```json
{
  "id": "127337d244834260",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286096,
  "host_pid": "9e6742732c60:1",
  "hash": "6a914f9bb13de5c20c1f1d16c51694a05e2e2ed3165db33bb450d42870449c73",
  "cid": "QmV16a914f9bb13de5c20c1f1d16c51694a05e2e2ed3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286096,
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
      "evaluated_at": 1760286096
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
  "sig": "159d26b86d5cdb464c986e0678f92250d916bf22105dfdd98ff8994649475882"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000248710981
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285763, 'matching_hash': '9a1c8fb9d78dcf4a'}}}