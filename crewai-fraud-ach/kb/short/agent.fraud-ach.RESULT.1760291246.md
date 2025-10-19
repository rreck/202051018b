```json
{
  "id": "23ea8281361f677a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291246,
  "host_pid": "9e6742732c60:1",
  "hash": "00cafeaec25670a18916beeab17aa00e122fd73223a471f50915f793048aca3b",
  "cid": "QmV100cafeaec25670a18916beeab17aa00e122fd732",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291246,
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
      "evaluated_at": 1760291246
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
  "sig": "9f471876c5403cb16e3777b02112307ac39edb431b3cab2b4d01f61dbe5f4a69"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 109883193945676
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 51188700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285765, 'matching_hash': '153e74d04ee716fe'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '109883192', 'validation_error': 'Invalid routing number checksum'}}}