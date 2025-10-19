```json
{
  "id": "434bead6a79e6df3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293390,
  "host_pid": "9e6742732c60:1",
  "hash": "963ef6e16fd8a9aec5b846dc7a229659a142037b22ab809982f2c7564bb575f7",
  "cid": "QmV1963ef6e16fd8a9aec5b846dc7a229659a142037b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293390,
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
      "evaluated_at": 1760293390
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
  "sig": "5e4479857a57c1a98d4746bf9ec62e02a85e1304b8c9645a10ec430f1f4558de"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 021000026914318
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 2123060730, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285765, 'matching_hash': '634436741ef501a5'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 91, 'details': {'zscore': 5.16, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9783690}}}