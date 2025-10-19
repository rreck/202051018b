```json
{
  "id": "9f7bd7bb5692e91f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287153,
  "host_pid": "9e6742732c60:1",
  "hash": "93ba38bdd2e33b765890e9258aa2411477c244e516443fd0ffcb77db4861fd2f",
  "cid": "QmV193ba38bdd2e33b765890e9258aa2411477c244e5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287153,
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
      "evaluated_at": 1760287153
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
  "sig": "1ba0beef3bf4a9a7dde27a8bdaa9f6d92ee3047b275a2ad1ca947243db7b2c8d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000022243585
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285764, 'matching_hash': '763c66b493018133'}}}re': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285764, 'matching_hash': '37b4044b8dabc650'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6602570}}}