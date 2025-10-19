```json
{
  "id": "4ff4ce9967d57ebd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289539,
  "host_pid": "9e6742732c60:1",
  "hash": "b080ca4c4d3a90bed8fe43ee59dafa20181ccd6fbccc0405bc5094be0058ebad",
  "cid": "QmV1b080ca4c4d3a90bed8fe43ee59dafa20181ccd6f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289539,
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
      "evaluated_at": 1760289539
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
  "sig": "79b9e90a0f301d794807d35ae084acff9e42b6f1154f989910920eba5e0b5e55"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467394934
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 42756966, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285763, 'matching_hash': '227a4380e23ca7de'}}}unt_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 1000000}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}