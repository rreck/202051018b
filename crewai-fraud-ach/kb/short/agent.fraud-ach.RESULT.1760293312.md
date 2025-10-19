```json
{
  "id": "dde3fde9ed4a219b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293312,
  "host_pid": "9e6742732c60:1",
  "hash": "c9586b88c9dc330d21a522eebc0024200df446185c06c74398ee6eeb8d1e4344",
  "cid": "QmV1c9586b88c9dc330d21a522eebc0024200df44618",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293312,
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
      "evaluated_at": 1760293312
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
  "sig": "41c3418a257c53942089791f3435b1d22e158a431c164f08d6f71ba14ce83f90"
}
```

Fraud detected: amount_anomaly (score: 85)
Transaction: 026009595171446
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 1399341744, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '6f6a57bfd56698c7'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.28, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6478434}}}