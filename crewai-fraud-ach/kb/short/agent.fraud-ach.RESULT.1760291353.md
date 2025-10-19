```json
{
  "id": "f9c8a75c4fd56142",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291353,
  "host_pid": "9e6742732c60:1",
  "hash": "fd1afad5a838af3ef1be58146bf9886aaa62c5ccc8f36254eb8756fe9be033e0",
  "cid": "QmV1fd1afad5a838af3ef1be58146bf9886aaa62c5cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291353,
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
      "evaluated_at": 1760291353
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
  "sig": "3aeecf49c10c9c511eaba9685b9cd77e218a4e65435f0716c9253a26e8da9aba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025664709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 17809831, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285764, 'matching_hash': '5cc83e27ca9ca801'}}}