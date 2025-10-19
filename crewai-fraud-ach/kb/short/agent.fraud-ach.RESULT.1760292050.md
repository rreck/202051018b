```json
{
  "id": "84976d2bd3f1cd95",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292050,
  "host_pid": "9e6742732c60:1",
  "hash": "70261df6e7e48a567be43a8ad3d60e294ecae0789d43e3a235011f89605aa4bc",
  "cid": "QmV170261df6e7e48a567be43a8ad3d60e294ecae078",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292050,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760292050
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "12e127ef238aa9075158d3fbd833340b2cfdc0bd646d425f2260fb6c64b30e9b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460526260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 67539150, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': '4d7dea8b6c0fe79e'}}}