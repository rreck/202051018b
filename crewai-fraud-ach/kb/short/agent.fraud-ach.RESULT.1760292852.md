```json
{
  "id": "408dbd8c259a47a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292852,
  "host_pid": "9e6742732c60:1",
  "hash": "20d279a3c0b2c6c860d465cc2dde6f415a09227b4193a20e1f2e1dd19dcf9d2c",
  "cid": "QmV120d279a3c0b2c6c860d465cc2dde6f415a09227b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292852,
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
      "evaluated_at": 1760292852
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "4e8300ffe3b3ba96cecd0a37c9453de0528a332eb859d6e10d8cf4662b95edb9"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 031201467949832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 206000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285764, 'matching_hash': '3eb2ce6b003836d6'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}