```json
{
  "id": "4cfc3db6560ffb26",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287515,
  "host_pid": "9e6742732c60:1",
  "hash": "e5128f9131ea9d8cce6ab44d0d3b843af955620a345f3c5b358fe6a4469aabd0",
  "cid": "QmV1e5128f9131ea9d8cce6ab44d0d3b843af955620a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287515,
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
      "evaluated_at": 1760287515
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
  "sig": "547b648049e2c525668c5e0ba669598da6145ebd206bde628137da6cf5ff3a98"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 122105152274101
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 11302389, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285763, 'matching_hash': 'b0ffab0948116893'}}}