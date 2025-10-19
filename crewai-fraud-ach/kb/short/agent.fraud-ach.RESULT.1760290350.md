```json
{
  "id": "29021006326b1c66",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290350,
  "host_pid": "9e6742732c60:1",
  "hash": "db3f6252feca1dbbd8cc74572b42487e87961b3b7940bfaaa83d4dea0b1359e0",
  "cid": "QmV1db3f6252feca1dbbd8cc74572b42487e87961b3b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290350,
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
      "evaluated_at": 1760290350
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
  "sig": "f7b60ec3ab94aca51dc57a89e8703ae12d0d55e8672518eb55a1748efe3b97a4"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 113877664521121
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 53467960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': '0cc689f8838aa314'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '113877666', 'validation_error': 'Invalid routing number checksum'}}}