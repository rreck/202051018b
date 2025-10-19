```json
{
  "id": "a2d37fa2fbf990ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294197,
  "host_pid": "9e6742732c60:1",
  "hash": "833d59373b6743bc9906cc78f03b4ff192f677b8c8a24dbbe359c279145f300a",
  "cid": "QmV1833d59373b6743bc9906cc78f03b4ff192f677b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294197,
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
      "evaluated_at": 1760294197
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
  "sig": "00f24d33490b2a70472f545ee667156f154f252871919cbaaeeeeadcfe5913f4"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 121000242463666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 1820960939, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285764, 'matching_hash': '3cd63f27035973d0'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 80, 'details': {'zscore': 4.04, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 7815283}}}