```json
{
  "id": "99f18f8e96f909fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291666,
  "host_pid": "9e6742732c60:1",
  "hash": "435fc323bd851331094b4bd3f60d24daac0d99025937241d5f442004809c70a9",
  "cid": "QmV1435fc323bd851331094b4bd3f60d24daac0d9902",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291666,
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
      "evaluated_at": 1760291666
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
  "sig": "13f0e8a15bbee861426672cf677da311d612bcd705434c9ce0b1776c502afe07"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 039274533993332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 29333340, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285765, 'matching_hash': 'a2ad50f9b8d4dabc'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '039274537', 'validation_error': 'Invalid routing number checksum'}}}