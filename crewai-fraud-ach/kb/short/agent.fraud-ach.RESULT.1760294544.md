```json
{
  "id": "45dd57a55c66987a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294544,
  "host_pid": "9e6742732c60:1",
  "hash": "dd4397ad45656041539dcc0a82b50c2c893d064689cce3028c31fb60938b04df",
  "cid": "QmV1dd4397ad45656041539dcc0a82b50c2c893d0646",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294544,
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
      "evaluated_at": 1760294544
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "45b37ffcca15a002902f3b1e951e2f31cc08e1fe638be2965ed1356fbd25fc4b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464554990
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 65547120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': 'ab9afd20a22fc7b8'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '020899456', 'validation_error': 'Invalid routing number checksum'}}}