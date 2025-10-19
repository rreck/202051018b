```json
{
  "id": "a1c08cb834c5ff63",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294721,
  "host_pid": "9e6742732c60:1",
  "hash": "8703406e4170fbf5eb1baff98a7abad9d18a5db6375204350ff2068ff2af8021",
  "cid": "QmV18703406e4170fbf5eb1baff98a7abad9d18a5db6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294721,
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
      "evaluated_at": 1760294721
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
  "sig": "66319e7b393f448243ba5ffd41c545116081c43d2ce8217c369c5c1315dd18c5"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 818309298369568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 114479730, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285765, 'matching_hash': '9e3984c977816ea5'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '818309298', 'validation_error': 'Invalid routing number checksum'}}}