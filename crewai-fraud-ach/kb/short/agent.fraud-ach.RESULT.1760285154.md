```json
{
  "id": "eedc40a94c869c6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285154,
  "host_pid": "9e6742732c60:1",
  "hash": "0d7acee2e5492f43e06ac10aa33b10cb4f562a67f8a20d8a83cd776b972895f1",
  "cid": "QmV10d7acee2e5492f43e06ac10aa33b10cb4f562a67",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285154,
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
      "evaluated_at": 1760285154
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
  "sig": "eeec7f430cf1292be28335c711a9f3771d93f1630e944140b5cd6a4a7d234588"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000036487644
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760284979, 'matching_hash': '0d42dcc750e3a553'}}}