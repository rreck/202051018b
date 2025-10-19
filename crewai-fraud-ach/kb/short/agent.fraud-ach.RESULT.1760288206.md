```json
{
  "id": "9a5ef274f1e10f1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288206,
  "host_pid": "9e6742732c60:1",
  "hash": "ea128e5932c0aed815eb59b370a3fc4b11e63ba87872dde96a45e7d0756eba7d",
  "cid": "QmV1ea128e5932c0aed815eb59b370a3fc4b11e63ba8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288206,
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
      "evaluated_at": 1760288206
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
  "sig": "6c4149ea77d67df232ddfe3646d2f3e4e1fc17f645154dae0d2cb51bf5cf2bfe"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 063100275656907
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 592752334, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285764, 'matching_hash': '3d5aab5dd753a251'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6892469}}}