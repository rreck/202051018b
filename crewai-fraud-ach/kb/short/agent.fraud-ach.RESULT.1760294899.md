```json
{
  "id": "fad0caafa411cb1e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294899,
  "host_pid": "9e6742732c60:1",
  "hash": "78875f1379e8277a9381da1dc94fe56ba02e9b19d22afae53a9c73aad34586ad",
  "cid": "QmV178875f1379e8277a9381da1dc94fe56ba02e9b19",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294899,
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
      "evaluated_at": 1760294899
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "24c4f927110fe864062ddedc6a5f801be011895916b59150485c64f8be37d40c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 635242948975660
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 105709152, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285765, 'matching_hash': '596a6d950333709b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '635242942', 'validation_error': 'Invalid routing number checksum'}}}