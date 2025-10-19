```json
{
  "id": "e1db7b1afaf5116a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292711,
  "host_pid": "9e6742732c60:1",
  "hash": "24ef9a18e4a500f5953e60f29e19707d280aca31010fa0a7c58c5e656bf248cd",
  "cid": "QmV124ef9a18e4a500f5953e60f29e19707d280aca31",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292711,
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
      "evaluated_at": 1760292711
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
  "sig": "827449fce730d5f7ec167ff1159a3425e632ade8a20fc55466bc6641e838c97c"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 021000026312877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 1144678227, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285764, 'matching_hash': 'b3443459d853f7b8'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5638809}}}