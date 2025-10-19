```json
{
  "id": "1f8e3b47dc48dc87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287263,
  "host_pid": "9e6742732c60:1",
  "hash": "c478f7a8c59ce36fa0f3ef2bda5b70203ae0ca09be46cb887b4e5d09c9459d6c",
  "cid": "QmV1c478f7a8c59ce36fa0f3ef2bda5b70203ae0ca09",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287263,
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
      "evaluated_at": 1760287263
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_high"
  ],
  "sig": "99dc25cbef0f6aa7ff6170dea2602d108e35f2804315850c7073fba83445762f"
}
```

Fraud detected: amount_anomaly (score: 76)
Transaction: 063100270720281
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 54, 'threshold': 50, 'total_amount': 498809394, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285763, 'matching_hash': 'aab950dc161fb34f'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 75, 'details': {'zscore': 3.5, 'mean': 1373847.7, 'stdev': 2245589.6016213675, 'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 9237211}}}