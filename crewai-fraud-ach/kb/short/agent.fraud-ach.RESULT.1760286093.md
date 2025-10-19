```json
{
  "id": "c1cc7caaa4102d2e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286093,
  "host_pid": "9e6742732c60:1",
  "hash": "ca8c0830d0207a3bf68405854f2cc4bc7ab9ffdaf3e887415e7e7f840fe6c16a",
  "cid": "QmV1ca8c0830d0207a3bf68405854f2cc4bc7ab9ffda",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286093,
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
      "evaluated_at": 1760286093
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
  "sig": "798827bc3ca0ae138734ded819e5ba65bad9feece35b9592cd29300ea0afa92f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201463621906
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285763, 'matching_hash': 'c1b23d91813533f7'}}}