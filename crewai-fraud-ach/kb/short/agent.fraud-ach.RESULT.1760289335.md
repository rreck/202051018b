```json
{
  "id": "47d547d943905af4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289335,
  "host_pid": "9e6742732c60:1",
  "hash": "c20693d45d54712ce6a54858904eb84d213bde4bd7318c9e8d132471d9cceb5a",
  "cid": "QmV1c20693d45d54712ce6a54858904eb84d213bde4b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289335,
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
      "evaluated_at": 1760289335
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
  "sig": "12a2b85560ec7c31a568436ca95b841f497e2c9cbf4597444914520fd6b920b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025121499
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 15265560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285763, 'matching_hash': 'a696ea0f650f1de2'}}}