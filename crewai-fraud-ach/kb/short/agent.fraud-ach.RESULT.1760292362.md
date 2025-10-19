```json
{
  "id": "ac015c8c4d2185f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292362,
  "host_pid": "9e6742732c60:1",
  "hash": "58d37cc7f360071f70e2c2fd11b3aa3f6f740ea255bea964c692023549bbd537",
  "cid": "QmV158d37cc7f360071f70e2c2fd11b3aa3f6f740ea2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292362,
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
      "evaluated_at": 1760292362
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
  "sig": "06c8366ed3b90699a1c37c625023fa3bd52fd2458de3b71de62e6dbd5b107ad7"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 041887157928370
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 85252748, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': '40835df504bb3fdd'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '041887155', 'validation_error': 'Invalid routing number checksum'}}}