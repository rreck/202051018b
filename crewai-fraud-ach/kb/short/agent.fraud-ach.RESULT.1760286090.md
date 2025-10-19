```json
{
  "id": "228924ff86866339",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286090,
  "host_pid": "9e6742732c60:1",
  "hash": "396dc29c1e2b4f07dd033a973e61a7b00bc010da6d062e48bf1523e911909bcf",
  "cid": "QmV1396dc29c1e2b4f07dd033a973e61a7b00bc010da",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286090,
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
      "evaluated_at": 1760286090
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
  "sig": "f84ec84984377fd4933ea38d69a6ee50d976998e1baba1adee612941b272db0b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201463891034
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285763, 'matching_hash': '2167bcd96d131e8f'}}}