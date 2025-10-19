```json
{
  "id": "3180ec445780c6a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290402,
  "host_pid": "9e6742732c60:1",
  "hash": "713bf5b42245cce17919ad3ab4e9999a0a65842392acd170b091a849f621f280",
  "cid": "QmV1713bf5b42245cce17919ad3ab4e9999a0a658423",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290402,
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
      "evaluated_at": 1760290402
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
  "sig": "1ba9269a43dbf01489ff946d931ea683ec777cb543a887de02c36b6783a8fc55"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 063100273946283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 1445364070, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285765, 'matching_hash': 'ff0c3c22534c93d5'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.11, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9700430}}}