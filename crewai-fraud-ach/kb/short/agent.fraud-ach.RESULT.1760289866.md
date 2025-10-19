```json
{
  "id": "37170bbd2b707f8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289866,
  "host_pid": "9e6742732c60:1",
  "hash": "e33f99b8f3f79795dd6f8535eef9f3decffa434ac92c4dcea7bda288f7fb87af",
  "cid": "QmV1e33f99b8f3f79795dd6f8535eef9f3decffa434a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289866,
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
      "evaluated_at": 1760289866
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
  "sig": "f16bbd8fabf87b4487c4b855ddb5c6a1e69af2088db9e3008213df87a8ac51a6"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 671070000820328
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 47240790, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760284979, 'matching_hash': '6a7cc3d9f67da590'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '671070002', 'validation_error': 'Invalid routing number checksum'}}}