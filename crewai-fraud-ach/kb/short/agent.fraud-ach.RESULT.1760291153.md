```json
{
  "id": "3ef0553b09814daf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291153,
  "host_pid": "9e6742732c60:1",
  "hash": "49b468d4685f14c74bc8e4789d73213e3564c1648652db4efa96a083d1483a66",
  "cid": "QmV149b468d4685f14c74bc8e4789d73213e3564c164",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291153,
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
      "evaluated_at": 1760291153
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
  "sig": "2ddececcf7621a76b2b348d72662fc80fcd4a14f0cb0c81fa79751d6cdb988ad"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 818309298369568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 79146480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285765, 'matching_hash': '9e3984c977816ea5'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818309298', 'validation_error': 'Invalid routing number checksum'}}}