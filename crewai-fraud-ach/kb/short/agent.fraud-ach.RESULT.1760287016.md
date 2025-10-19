```json
{
  "id": "a462abdc3aad9403",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287016,
  "host_pid": "9e6742732c60:1",
  "hash": "47ca8e9865da6f1008d0562ca55e78e1fa77f6f4f76e00f4a9c0b43703541f61",
  "cid": "QmV147ca8e9865da6f1008d0562ca55e78e1fa77f6f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287016,
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
      "evaluated_at": 1760287016
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
  "sig": "95a8ec9ff42d75e6bf910d4bf5ef6b08df56703dfa95d52eb39765b9ceadd544"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100270534223
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285765, 'matching_hash': '6dd341e8ae885101'}}}