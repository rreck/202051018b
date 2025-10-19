```json
{
  "id": "834af4173768fc26",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290555,
  "host_pid": "9e6742732c60:1",
  "hash": "d3d4081110a3be9fcd554d20c77e1082dae1811eadc73f87c813ed97946641d0",
  "cid": "QmV1d3d4081110a3be9fcd554d20c77e1082dae1811e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290555,
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
      "evaluated_at": 1760290555
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
  "sig": "57504672039bf20dd0830dceec223025d9c8388ac73c281afc2fa536c9193ca8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598542542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 51171003, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285764, 'matching_hash': '3cc1c7bbce52acf6'}}}