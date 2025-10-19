```json
{
  "id": "a13bdd3b94a811e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288377,
  "host_pid": "9e6742732c60:1",
  "hash": "10c3a8476f131e4be8ca2ef1fd21140ad4f33e7a84e8b9393481e769205fcb99",
  "cid": "QmV110c3a8476f131e4be8ca2ef1fd21140ad4f33e7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288377,
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
      "evaluated_at": 1760288377
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
  "sig": "7a57a3fe60ab612bc04055931be29e106b8f6ab0ffabe07ac5200c129054ce32"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028970082
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 25814425, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285765, 'matching_hash': 'a98af89fc7548453'}}}