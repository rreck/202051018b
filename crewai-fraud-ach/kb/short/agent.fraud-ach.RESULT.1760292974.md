```json
{
  "id": "85936a20641b7ce4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292974,
  "host_pid": "9e6742732c60:1",
  "hash": "3300fa930ad77c92c571cbd472c498e4a8710fec68435edeb6f710cd06f0ab35",
  "cid": "QmV13300fa930ad77c92c571cbd472c498e4a8710fec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292974,
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
      "evaluated_at": 1760292974
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
  "sig": "e4fca4303df55f5c77710efb562c2efaeeb8947c862bc2a73dd468059e1b3654"
}
```

Fraud detected: amount_anomaly (score: 91)
Transaction: 111000023855884
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 1966875801, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '29f4fac8ca9c8442'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 89, 'details': {'zscore': 4.95, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 9410889}}}