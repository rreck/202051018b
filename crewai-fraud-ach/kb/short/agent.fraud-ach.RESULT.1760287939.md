```json
{
  "id": "ba46e3e8f544f728",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287939,
  "host_pid": "9e6742732c60:1",
  "hash": "d328f93afbdf5aeebed92dc6b63231cd55655f191dc42de3109ed5e70d22eeaa",
  "cid": "QmV1d328f93afbdf5aeebed92dc6b63231cd55655f19",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287939,
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
      "evaluated_at": 1760287939
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
  "sig": "0c93df83f464b7040acbd50972643057e867114cd08d349bc75cf7b6e3dfcfe7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025883497
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 24486308, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285765, 'matching_hash': '8c29ee71720a2634'}}}