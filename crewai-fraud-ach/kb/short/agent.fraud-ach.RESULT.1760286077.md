```json
{
  "id": "f5cc1a050f76ab7b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286077,
  "host_pid": "9e6742732c60:1",
  "hash": "95fb96d3e00582367db3c926503610d5800fcc8f20f9eaba017c85e4b3e21437",
  "cid": "QmV195fb96d3e00582367db3c926503610d5800fcc8f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286077,
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
      "evaluated_at": 1760286077
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
  "sig": "c72c1d58bde27a198f1eb5ab63c767497111eee5bac902a9a3bbf2cf6914afc6"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}