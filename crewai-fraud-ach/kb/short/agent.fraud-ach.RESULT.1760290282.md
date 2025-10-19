```json
{
  "id": "83f9f4c04a751a55",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290282,
  "host_pid": "9e6742732c60:1",
  "hash": "01cb3671d76c93741d29e57e6af9383e09768589dc7d833120f07cfa1b01cf50",
  "cid": "QmV101cb3671d76c93741d29e57e6af9383e09768589",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290282,
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
      "evaluated_at": 1760290282
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
  "sig": "3ee740fefd2742e861f281e250b017023957075dbcf75760c37cc8ac1b55c60e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241978752
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 32646038, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285765, 'matching_hash': '600b54b59692179b'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}