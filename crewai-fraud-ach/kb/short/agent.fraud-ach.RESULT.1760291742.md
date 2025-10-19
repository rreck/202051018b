```json
{
  "id": "5c6eb5a39cb7ae8a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291742,
  "host_pid": "9e6742732c60:1",
  "hash": "077da543eb91fb981ead003ae12c921b1741e17686144f945a5f6c9ee5942219",
  "cid": "QmV1077da543eb91fb981ead003ae12c921b1741e176",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291742,
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
      "evaluated_at": 1760291742
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
  "sig": "2042eeddbcf9db068c1da72bbbc34d95f7cd1403305b88ea354ee1dcc21f2108"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 113877664521121
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 65751140, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285763, 'matching_hash': '0cc689f8838aa314'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '113877666', 'validation_error': 'Invalid routing number checksum'}}}