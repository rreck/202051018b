```json
{
  "id": "8080575039c01e09",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292973,
  "host_pid": "9e6742732c60:1",
  "hash": "f993561523049f83010687b562099dee3953ab6917ba3242d532acd1f97bf3c0",
  "cid": "QmV1f993561523049f83010687b562099dee3953ab69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292973,
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
      "evaluated_at": 1760292974
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
  "sig": "4c4fe5a9540b93891c27752a59498c7f693af66152dab5dcd6010fccd48764f3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461090276
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 54160260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '697ecd0ef10c625b'}}}