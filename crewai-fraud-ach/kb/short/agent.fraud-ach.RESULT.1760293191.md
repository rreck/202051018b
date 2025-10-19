```json
{
  "id": "94e2a410fa573810",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293191,
  "host_pid": "9e6742732c60:1",
  "hash": "9beeed3c58819b0414937ac8db30726aeb08397c2ba36d59bfa034bdf8abc30d",
  "cid": "QmV19beeed3c58819b0414937ac8db30726aeb08397c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293191,
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
      "evaluated_at": 1760293191
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
  "sig": "b8a2db02dbd3e4ec7338b545ff6e661bcd1123cd8f0dee42ba601133955f0003"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039663431
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 31720599, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285764, 'matching_hash': '33f644fe289ea89d'}}}