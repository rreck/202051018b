```json
{
  "id": "3a51b0d40f8188d0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288888,
  "host_pid": "9e6742732c60:1",
  "hash": "a00eff4eb03dd98a6cec1e34e3a673e193284a97161ee67ce4db5098e70390f4",
  "cid": "QmV1a00eff4eb03dd98a6cec1e34e3a673e193284a97",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288888,
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
      "evaluated_at": 1760288888
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
  "sig": "61c078fff498ba7fbaa63b32df65388b9eb13626ae0700adfe553d17ad671654"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 607486347609576
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 46817957, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285763, 'matching_hash': '01e47067eb24b5e9'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '607486349', 'validation_error': 'Invalid routing number checksum'}}}