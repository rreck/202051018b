```json
{
  "id": "80a0f04b0f810bda",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289019,
  "host_pid": "9e6742732c60:1",
  "hash": "cfd3bc697b99e6ca9b087f66b9fd3ede22cffa9e8ebaed9a80b29cd414649daa",
  "cid": "QmV1cfd3bc697b99e6ca9b087f66b9fd3ede22cffa9e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289019,
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
      "evaluated_at": 1760289019
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
  "sig": "7e58304da83dd764b79de3dfc6f78077ee8673a129e6e2c91bde4fbcd5e92cd2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023390591
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 34743444, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285764, 'matching_hash': '65b6a0d7e3017724'}}}