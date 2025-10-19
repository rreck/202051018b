```json
{
  "id": "ce851a3a8b8f0426",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291412,
  "host_pid": "9e6742732c60:1",
  "hash": "183987d07d885267a0c2c11f30ab5445a7a3dca71469a34cd15279f6366e3397",
  "cid": "QmV1183987d07d885267a0c2c11f30ab5445a7a3dca7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291412,
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
      "evaluated_at": 1760291412
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
  "sig": "3ead5b3f254b51b78bd1fae64192ad74f879d011e4bd7dd766821de35293b7a8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023546405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 74981298, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': '22f38bfa79b47563'}}}