```json
{
  "id": "da786d15b418a5b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290425,
  "host_pid": "9e6742732c60:1",
  "hash": "db1edcd8f6b6961665a1b1329bed6fa25e89b342c9ee58852eb50408521edf84",
  "cid": "QmV1db1edcd8f6b6961665a1b1329bed6fa25e89b342",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290425,
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
      "evaluated_at": 1760290425
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
  "sig": "7bc7d480c5105c781a8462156c5d75f77dc77a141aa9a510c8642219bc544ec5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462273667
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 66973050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': 'db56bbc4ded669a9'}}}