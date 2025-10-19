```json
{
  "id": "369e4e10cd651e29",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290429,
  "host_pid": "9e6742732c60:1",
  "hash": "ba20aede9e8ce2216eb7bb7e748ea78375a147e0be83ed53bf1acc560e0f45f0",
  "cid": "QmV1ba20aede9e8ce2216eb7bb7e748ea78375a147e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290429,
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
      "evaluated_at": 1760290429
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
  "sig": "b3c2aeefee1657cdd3627a01233ef657825e720cfd3d95c12cb82792ec6b8cc5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156085799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 35442900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': 'a879e580def76590'}}}