```json
{
  "id": "6394282f26a86889",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286608,
  "host_pid": "9e6742732c60:1",
  "hash": "566b38ee08c69ed33904b0f87447f81fbd860d2f80bdb0433f9c6ff2993fb2f7",
  "cid": "QmV1566b38ee08c69ed33904b0f87447f81fbd860d2f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286608,
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
      "evaluated_at": 1760286608
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
  "sig": "130339cfe6fdbebd9dd10d0061ed271b70ac5dfa15cbf4b2b3e8482612beb5ed"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000037688830
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285764, 'matching_hash': 'a1e0090e71bf48f4'}}}re': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760285764, 'matching_hash': '13ee20e814facee3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.37, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 8942822}}}