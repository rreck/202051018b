```json
{
  "id": "4aa1f57bdae6dc05",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292903,
  "host_pid": "9e6742732c60:1",
  "hash": "089aacec067665aaf63b8f6f09b7cc6bb53feb7538e9267319bd96c7626d82ab",
  "cid": "QmV1089aacec067665aaf63b8f6f09b7cc6bb53feb75",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292903,
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
      "evaluated_at": 1760292903
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
  "sig": "c94bec35a123505586d8bc533a11edf3d02509ae4dafa19a1c4cd2ce539d5489"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 026009598348562
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 1735095114, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285765, 'matching_hash': '08c1aa7df797b6df'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 83, 'details': {'zscore': 4.36, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8382102}}}