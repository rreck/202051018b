```json
{
  "id": "2d9654f1d50234b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287867,
  "host_pid": "9e6742732c60:1",
  "hash": "e7ff13304aebefde92ccffe331e0eb4bcfaab827fdb8ad4532a9f050898904d5",
  "cid": "QmV1e7ff13304aebefde92ccffe331e0eb4bcfaab827",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287867,
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
      "evaluated_at": 1760287867
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
  "sig": "c63d2e80f42e48687d07da5afce7c1102861d0a059b2e724b7eddfbc87994fe5"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 646437634699290
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 33596400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285763, 'matching_hash': 'd218c468aa26fc36'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '646437635', 'validation_error': 'Invalid routing number checksum'}}}