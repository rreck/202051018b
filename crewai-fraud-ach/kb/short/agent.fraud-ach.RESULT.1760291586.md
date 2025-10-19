```json
{
  "id": "df5083974f9469d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291586,
  "host_pid": "9e6742732c60:1",
  "hash": "e3c6da662eb0a7e92ed4d8c3324cdd659ef6d4e2a3d7a5a36af4a43e912773a7",
  "cid": "QmV1e3c6da662eb0a7e92ed4d8c3324cdd659ef6d4e2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291586,
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
      "evaluated_at": 1760291586
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
  "sig": "b6bcc84ec7a8ac71ea38e6138fb9a71dcb638178639632b1089f1e92afca0183"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 121000249844926
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 935141156, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285765, 'matching_hash': '4f8c06dc9d4c212b'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5253602}}}