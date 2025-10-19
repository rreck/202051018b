```json
{
  "id": "46c98f61b1aa89b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286518,
  "host_pid": "9e6742732c60:1",
  "hash": "55ed281269b2685057ccc5d28b79b2b87c653a7805a2cb6ba6d15f52cdc42049",
  "cid": "QmV155ed281269b2685057ccc5d28b79b2b87c653a78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286518,
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
      "evaluated_at": 1760286518
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
  "sig": "d151b9a518919902b16e3bd44aa5b355322795135f302fb38b268e7c34e47bf1"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105150128981
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 27, 'first_seen': 1760285763, 'matching_hash': '59c56ba6c2207f9a'}}}