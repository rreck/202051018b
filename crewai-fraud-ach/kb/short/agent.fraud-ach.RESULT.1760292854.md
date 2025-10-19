```json
{
  "id": "20c7de86afbf51bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292854,
  "host_pid": "9e6742732c60:1",
  "hash": "667b0cb3a8e5010e958455c79ddae525b8b4b8823d7849b9cb294e099cfe9df0",
  "cid": "QmV1667b0cb3a8e5010e958455c79ddae525b8b4b882",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292854,
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
      "evaluated_at": 1760292854
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
  "sig": "991fbb35489dfc4df28a53f2faf64cba31b08fff54f7abd7b9f6e150ccb46ed3"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 021000026312877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 1161594654, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285764, 'matching_hash': 'b3443459d853f7b8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5638809}}}