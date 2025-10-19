```json
{
  "id": "19488fcdf7a2a037",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293681,
  "host_pid": "9e6742732c60:1",
  "hash": "39f214bffbc10fab55097ab7e3395d33ba1281c75cc9fbb25ab48f2fead6302c",
  "cid": "QmV139f214bffbc10fab55097ab7e3395d33ba1281c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293681,
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
      "evaluated_at": 1760293681
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
  "sig": "9e063667a519e80e9616947be7bba4c8e816c918053058e1a7abd4e67130676a"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 478694940117269
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 43177260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285764, 'matching_hash': 'c8ebc968ccc74844'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '478694940', 'validation_error': 'Invalid routing number checksum'}}}