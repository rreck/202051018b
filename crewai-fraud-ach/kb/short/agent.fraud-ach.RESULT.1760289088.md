```json
{
  "id": "5af8eb4ba4509854",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289088,
  "host_pid": "9e6742732c60:1",
  "hash": "7a81ac3fa588e80b85113c0437b3745292af74c28585d3b0f3b93e3d58dbf007",
  "cid": "QmV17a81ac3fa588e80b85113c0437b3745292af74c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289088,
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
      "evaluated_at": 1760289088
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "9160f322e4e939ff1050c5ef9336d17caf085c93571f62cdd905547adc4a6c36"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026198505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 52929313, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285764, 'matching_hash': '8ff7ad30241d2e02'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}