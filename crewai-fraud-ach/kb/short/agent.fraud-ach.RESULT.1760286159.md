```json
{
  "id": "2945591117306982",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286159,
  "host_pid": "9e6742732c60:1",
  "hash": "c5cb3e2c5fab4af5077e806af12b764618d2038142ed5b3d7b364c33b33bc6c3",
  "cid": "QmV1c5cb3e2c5fab4af5077e806af12b764618d20381",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286159,
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
      "evaluated_at": 1760286159
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
  "sig": "8947045cb10f93a0b4da0cecc56d80b29759c780b8b15311143fa3d002cf456b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156760115
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 15, 'first_seen': 1760285764, 'matching_hash': '84a7174d04c2e814'}}}