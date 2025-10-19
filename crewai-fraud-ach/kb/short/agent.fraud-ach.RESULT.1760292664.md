```json
{
  "id": "0008b2c6258104cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292664,
  "host_pid": "9e6742732c60:1",
  "hash": "33f3e12cef313aa598a6b5b3df3767936574dc8ab8d33605dece85a159543387",
  "cid": "QmV133f3e12cef313aa598a6b5b3df3767936574dc8a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292664,
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
      "evaluated_at": 1760292664
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
  "sig": "0ca78d83cbb4db1c9ec02ac08fb4a20a810f152ccd411783868df908b52eed57"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 011137004104696
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 24651878, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285765, 'matching_hash': 'b4a76c6b789f42f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '011137004', 'validation_error': 'Invalid routing number checksum'}}}