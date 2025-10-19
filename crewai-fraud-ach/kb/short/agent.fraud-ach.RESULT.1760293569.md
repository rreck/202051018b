```json
{
  "id": "61ab73a179f3cc78",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293569,
  "host_pid": "9e6742732c60:1",
  "hash": "ed244bce0ee7c401b61497071301d2ec1c49c91d0c8e623b972b9ddfd149d73c",
  "cid": "QmV1ed244bce0ee7c401b61497071301d2ec1c49c91d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293569,
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
      "evaluated_at": 1760293569
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
  "sig": "c1d51d939866b8f05118f0884c65dff477d11c0f139833a46b24d73bcd67b557"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 291093508895399
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 104954668, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': 'b750a26a60b25ace'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '291093507', 'validation_error': 'Invalid routing number checksum'}}}