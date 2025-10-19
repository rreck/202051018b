```json
{
  "id": "3656123f34c1e623",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289444,
  "host_pid": "9e6742732c60:1",
  "hash": "755cafe132b1ecd36d0ffd2892b7897711ee5fe34e1b97924a24e126f78d77dc",
  "cid": "QmV1755cafe132b1ecd36d0ffd2892b7897711ee5fe3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289444,
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
      "evaluated_at": 1760289444
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "7d078be44e590cd400f4137c5f56f2ad41c99226c03a0299ac277d7dc834c2eb"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 121000240089409
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 755100690, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285765, 'matching_hash': 'a79d0bf31de09717'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 70, 'details': {'zscore': 3.08, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 6139030}}}