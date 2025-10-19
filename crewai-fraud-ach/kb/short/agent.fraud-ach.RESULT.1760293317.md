```json
{
  "id": "a265538530552f2a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293317,
  "host_pid": "9e6742732c60:1",
  "hash": "07d880b07cd9a40d6063f1f71679d542daff80424d99485788c93536810f4fb2",
  "cid": "QmV107d880b07cd9a40d6063f1f71679d542daff8042",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293317,
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
      "evaluated_at": 1760293317
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
  "sig": "a0bfbe3d70c4a305bcc044fdd5478e1efb5ebd3ca1406e95dfd58ef6da6bb8ba"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 614505621863127
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 59962032, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285764, 'matching_hash': '8748c624c8dfcb5e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '614505622', 'validation_error': 'Invalid routing number checksum'}}}