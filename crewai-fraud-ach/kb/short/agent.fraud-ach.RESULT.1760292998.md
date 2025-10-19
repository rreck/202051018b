```json
{
  "id": "f6f30a9cf59d53f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292998,
  "host_pid": "9e6742732c60:1",
  "hash": "7294eab20edcbe8f7d34240acc5c08e1df32e4f73275b32f1d5eb4ebd48fb4a7",
  "cid": "QmV17294eab20edcbe8f7d34240acc5c08e1df32e4f7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292998,
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
      "evaluated_at": 1760292998
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
  "sig": "030de2d3453820fea4e5b334ebda6350710a0c026b8d3f7bd3df043190562756"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 031201464331888
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 1323548303, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285764, 'matching_hash': '6a7d940bcd4512ca'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 71, 'details': {'zscore': 3.19, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6332767}}}