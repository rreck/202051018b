```json
{
  "id": "b00fef55afde8e2a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293906,
  "host_pid": "9e6742732c60:1",
  "hash": "bd2ad374e298fe5b7d905d380583f18ca8d9547306626f40fa586c4fcc1b6794",
  "cid": "QmV1bd2ad374e298fe5b7d905d380583f18ca8d95473",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293906,
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
      "evaluated_at": 1760293906
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
  "sig": "efffe633a51221070f9b1c398d24a4ef5d55523821427495a2d5ef299b6c772c"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000023922367
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 1358061252, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': '420dc08dc8ad4808'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 5956409}}}