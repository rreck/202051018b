```json
{
  "id": "109461be4fcc879b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286275,
  "host_pid": "9e6742732c60:1",
  "hash": "d0de825e414872840ace36e6d8bb5633bf3bd50bc7b835776ad2b78c96211bb6",
  "cid": "QmV1d0de825e414872840ace36e6d8bb5633bf3bd50b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286275,
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
      "evaluated_at": 1760286275
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
  "sig": "b04f4454014dbf8d98f378f2755d272f5d0dc77f674440c8f91b411f96960d72"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201465949521
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285763, 'matching_hash': '5db5b45722d53397'}}}