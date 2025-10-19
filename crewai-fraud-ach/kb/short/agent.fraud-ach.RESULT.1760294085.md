```json
{
  "id": "3de0f0bb81c5dff6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294085,
  "host_pid": "9e6742732c60:1",
  "hash": "35ac3ab0be51292f3efa94ed387b2c14ae1e1db6e11e85e46394a91f99d498f3",
  "cid": "QmV135ac3ab0be51292f3efa94ed387b2c14ae1e1db6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294085,
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
      "evaluated_at": 1760294085
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
  "sig": "6e42e424fbeabb63a3f94d42495bc2fd171e821f44aefb68aa451e80b48d405b"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 906924177607497
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 59595921, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285765, 'matching_hash': 'a0bedab775ea6194'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '906924178', 'validation_error': 'Invalid routing number checksum'}}}