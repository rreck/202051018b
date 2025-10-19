```json
{
  "id": "714a1910a2ee7c57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289268,
  "host_pid": "9e6742732c60:1",
  "hash": "62f193f3a6d1cb4a9f994f37813347fc80052d366dc44051b4605890c088282a",
  "cid": "QmV162f193f3a6d1cb4a9f994f37813347fc80052d36",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289268,
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
      "evaluated_at": 1760289268
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
  "sig": "91ae20e3b3b95204103d5f9439b94c0da2c6dac73dda5136b846d678c5b69ce2"
}
```

Fraud detected: round_amount_pattern (score: 71)
Transaction: 021000026547506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 118000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285764, 'matching_hash': 'e0a909ce459a76c8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}