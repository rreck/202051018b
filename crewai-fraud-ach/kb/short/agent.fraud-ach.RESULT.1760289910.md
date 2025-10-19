```json
{
  "id": "a22534a8e3e411df",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289910,
  "host_pid": "9e6742732c60:1",
  "hash": "ca5d852259f0c421e397ae1ed2fb25adde7b45d9912bb3bcdfdd91bb19150fb0",
  "cid": "QmV1ca5d852259f0c421e397ae1ed2fb25adde7b45d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289910,
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
      "evaluated_at": 1760289910
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
  "sig": "e0cc8c8ae08cc79161f4ac9d9ef04fa39399caf3be94b81fbede353a6bd0bbf6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270344488
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50, 'total_amount': 36278408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285764, 'matching_hash': 'ec3de169da630728'}}}