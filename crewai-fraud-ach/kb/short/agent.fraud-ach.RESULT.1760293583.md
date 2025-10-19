```json
{
  "id": "19904d7a87e50846",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293583,
  "host_pid": "9e6742732c60:1",
  "hash": "65e78dbefa5bf857be670a2eb43d0e0d5d5b67fe2623bf41a2c23a8f97b4e80d",
  "cid": "QmV165e78dbefa5bf857be670a2eb43d0e0d5d5b67fe",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293583,
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
      "evaluated_at": 1760293583
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
  "sig": "16647645e4375f285f8f9fecbbb695256420daa3938dc463f8d9915a92dc2703"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 021000026312877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 1246176789, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285764, 'matching_hash': 'b3443459d853f7b8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5638809}}}