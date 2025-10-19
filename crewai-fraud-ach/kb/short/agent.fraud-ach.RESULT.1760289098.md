```json
{
  "id": "c782c0d0b2255e70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289098,
  "host_pid": "9e6742732c60:1",
  "hash": "d2cd630754b26e4b2fac5b409adb853180ea19442d2759ef7ec186162c78f2ae",
  "cid": "QmV1d2cd630754b26e4b2fac5b409adb853180ea1944",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289098,
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
      "evaluated_at": 1760289098
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
  "sig": "38cc84a06f01d9c37996a3ca206d04930df8baed39516c34e67f4cc24294f9ed"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 021000026312877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 637185417, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285764, 'matching_hash': 'b3443459d853f7b8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5638809}}}