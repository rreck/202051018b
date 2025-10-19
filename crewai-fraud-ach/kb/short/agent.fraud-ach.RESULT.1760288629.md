```json
{
  "id": "0e5fe858e83c95bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288629,
  "host_pid": "9e6742732c60:1",
  "hash": "e2b2e8106e31bc9f27c5f04e7a9d38750214f9350fb06cccfc9bfc422215e115",
  "cid": "QmV1e2b2e8106e31bc9f27c5f04e7a9d38750214f935",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288629,
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
      "evaluated_at": 1760288629
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
  "sig": "9a9bbe6018799eca64b1cfc9dd14cd949ae234098cf1441fed5db86fe6a5e41e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026451752
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 43169700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760284979, 'matching_hash': 'ed66d17e763eb837'}}}