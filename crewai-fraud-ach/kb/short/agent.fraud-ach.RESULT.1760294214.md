```json
{
  "id": "3db3dac1511395b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294214,
  "host_pid": "9e6742732c60:1",
  "hash": "a3d5819813587f23b07fb5aaa684dac2852a3f7e095f9c4d770360aa7a2b9d17",
  "cid": "QmV1a3d5819813587f23b07fb5aaa684dac2852a3f7e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294214,
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
      "evaluated_at": 1760294214
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
  "sig": "95595368f536acc7d46facc229f8d2930ac3acffffbd410783f392f757b7bc5f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599280040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 113907924, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '3242f38050bfb93d'}}}