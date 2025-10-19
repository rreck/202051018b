```json
{
  "id": "65ae37475a90d331",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286501,
  "host_pid": "9e6742732c60:1",
  "hash": "70539b0570f036b7861ab3c7914e7dbc7d3e9861da09caea96181c9d84be5efe",
  "cid": "QmV170539b0570f036b7861ab3c7914e7dbc7d3e9861",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286501,
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
      "evaluated_at": 1760286501
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
  "sig": "cb8854a6b2b6b3346299dcb1033c119a3339e88151a17af55833f28300d49758"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000025883497
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 26, 'first_seen': 1760285765, 'matching_hash': '8c29ee71720a2634'}}}