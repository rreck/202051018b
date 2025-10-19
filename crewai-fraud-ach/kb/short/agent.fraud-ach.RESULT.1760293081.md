```json
{
  "id": "7c91b8a5f4709f0c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293081,
  "host_pid": "9e6742732c60:1",
  "hash": "183de75a65fd62595ed68f09dadbfedc801ecc7f5a79eb1c26e7becdee1d48ef",
  "cid": "QmV1183de75a65fd62595ed68f09dadbfedc801ecc7f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293081,
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
      "evaluated_at": 1760293081
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
  "sig": "a0b2b090076c1ae6ec8ac0dacdbb5da0033c08aeb005e0cb5d16e041f68083c6"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 291093508895399
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 100205588, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': 'b750a26a60b25ace'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '291093507', 'validation_error': 'Invalid routing number checksum'}}}