```json
{
  "id": "5521e87a1a318fee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288574,
  "host_pid": "9e6742732c60:1",
  "hash": "f521e3ea848be93943f4f021feba2ab97989e3d35202c14acd97235bf4f1fc54",
  "cid": "QmV1f521e3ea848be93943f4f021feba2ab97989e3d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288574,
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
      "evaluated_at": 1760288574
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
  "sig": "93587d4d96156aa7937b52b891061adcae6dfa3f715a5b630464dd7b58697bf4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249254910
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 11077206, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285765, 'matching_hash': '80dc97a16e454830'}}}