```json
{
  "id": "026dafbf8f370ccf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292160,
  "host_pid": "9e6742732c60:1",
  "hash": "597b0a28f2ef9d8d98d51151c3af508732a6ede5103c3bf52b85f9f7e874c6b2",
  "cid": "QmV1597b0a28f2ef9d8d98d51151c3af508732a6ede5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292160,
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
      "evaluated_at": 1760292160
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
  "sig": "70c44a75c3e46a150dc0652672557be0aa1a6b8c7f8e593869a09cbabcf9abc2"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 272809904666410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 59388776, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285765, 'matching_hash': 'b8be43189937b834'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '272809901', 'validation_error': 'Invalid routing number checksum'}}}