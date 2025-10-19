```json
{
  "id": "e92d3bddca4b19b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292855,
  "host_pid": "9e6742732c60:1",
  "hash": "e67bc172c955c126c174dd4456179ad4d8b3fcf93550411c13827fe20df8dc4e",
  "cid": "QmV1e67bc172c955c126c174dd4456179ad4d8b3fcf9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292855,
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
      "evaluated_at": 1760292855
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
  "sig": "075171a2bd6f0a2c42f142608ca7776f70bc39ef2873d0c35960eebd27e3120d"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 063100273946283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 1998288580, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285765, 'matching_hash': 'ff0c3c22534c93d5'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.11, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9700430}}}