```json
{
  "id": "5247098536713dd5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286219,
  "host_pid": "9e6742732c60:1",
  "hash": "69236f9fcf38245af95e47acbe24a75b113bd67dac97f614bf007599ba0b7a06",
  "cid": "QmV169236f9fcf38245af95e47acbe24a75b113bd67d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286219,
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
      "evaluated_at": 1760286219
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
  "sig": "558e63d7e6c920c33bdd780fc7e1ac83832287aae1fba22ae078d2a8b85b2542"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201463568898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285764, 'matching_hash': '8016b691bce48ab1'}}}