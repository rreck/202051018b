```json
{
  "id": "921a7a5fbe12ab90",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292763,
  "host_pid": "9e6742732c60:1",
  "hash": "39b3423a913f66082c524db05a3b5427cd8bf9db71c501736dd79d0aa6065aa6",
  "cid": "QmV139b3423a913f66082c524db05a3b5427cd8bf9db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292763,
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
      "evaluated_at": 1760292763
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
  "sig": "f09e198c84add573a1fe64a5973cb64dfb73ce2a88d46437f7b14639be2d34fb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152240558
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 85059228, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285765, 'matching_hash': '0371944fd59dbf43'}}}