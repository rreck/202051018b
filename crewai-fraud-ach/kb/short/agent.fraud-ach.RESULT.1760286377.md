```json
{
  "id": "c7d3ad551c7e146c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286377,
  "host_pid": "9e6742732c60:1",
  "hash": "976a4fac67a8b7f50a8c19cd1159346ea37d3a2af4dc60dcc5e34e96c19d84b7",
  "cid": "QmV1976a4fac67a8b7f50a8c19cd1159346ea37d3a2a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286377,
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
      "evaluated_at": 1760286377
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
  "sig": "d703594398038d535b872164c41ed94b6bda82ff259317ea60571a216946293a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201463882943
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285765, 'matching_hash': '0eb18222520b1d39'}}}