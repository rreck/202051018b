```json
{
  "id": "9a6d1f1e0475d231",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293213,
  "host_pid": "9e6742732c60:1",
  "hash": "59fd717ce9b29b678b2b608f28fd91fbcd32089778802c13edcfca5c70d585b9",
  "cid": "QmV159fd717ce9b29b678b2b608f28fd91fbcd320897",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293213,
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
      "evaluated_at": 1760293213
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
  "sig": "49e38ea3aea7b2f61c42a9aacada7fc67106b9f5041cdd935d686d9e0b121094"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022866819
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 21400000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': '7f3c5046f4bcc1d0'}}}