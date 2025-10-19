```json
{
  "id": "138569f73e7c791c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290139,
  "host_pid": "9e6742732c60:1",
  "hash": "588fc5b5abef97489a0a38bf9b2c28d6b2d6df1e9db03279c53dc13d0cb7d04a",
  "cid": "QmV1588fc5b5abef97489a0a38bf9b2c28d6b2d6df1e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290139,
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
      "evaluated_at": 1760290139
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
  "sig": "6f46959c91b94e20c756c0b8cbcb1df736eb9d586ae584a659e90e76f7c00e7d"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 649338001689495
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 47279184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285765, 'matching_hash': '47ca0a67ca137c75'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '649338005', 'validation_error': 'Invalid routing number checksum'}}}