```json
{
  "id": "e6b41a3836fc6d1b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286612,
  "host_pid": "9e6742732c60:1",
  "hash": "a40eb1f86c66677ee5724e7a616b3c64c23b7cea614404b818cc987cba1d5bb3",
  "cid": "QmV1a40eb1f86c66677ee5724e7a616b3c64c23b7cea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286612,
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
      "evaluated_at": 1760286612
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
  "sig": "756932d394c9170de2d820565066d6b2e2c5f2df1afeb17baaed98808a54ae98"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000027165618
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285763, 'matching_hash': '01e7bf5fcf2bbeec'}}}: 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}'details': {'zscore': 3.2, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8549284}}}