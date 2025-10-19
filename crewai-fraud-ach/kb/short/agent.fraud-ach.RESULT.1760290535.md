```json
{
  "id": "a74387b38f3154e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290535,
  "host_pid": "9e6742732c60:1",
  "hash": "b048e8a44848f6b7153f6a4e4471ac0f8ba4344f4f2ccae7f4b9451e0d2c354e",
  "cid": "QmV1b048e8a44848f6b7153f6a4e4471ac0f8ba4344f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290535,
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
      "evaluated_at": 1760290535
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
  "sig": "bdb20cf6cb15b31fd63506d8e95815e58182ff9cbcb6f9b403ee093ffe9dfa06"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038823890
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 31967973, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': '81df70e06ca09887'}}}