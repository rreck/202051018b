```json
{
  "id": "95b922c7a00aad9b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286095,
  "host_pid": "9e6742732c60:1",
  "hash": "319929d284ce57bbccc9dba3c8f3de5ca190183bbf5cd92e53c4ccb45e047c5d",
  "cid": "QmV1319929d284ce57bbccc9dba3c8f3de5ca190183b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286095,
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
      "evaluated_at": 1760286095
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
  "sig": "afcddd4cf92d713dcae57623713838ef1409e4cba26a2b4f2d3cfe2334036e52"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000240116635
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285763, 'matching_hash': 'faa8e9f78afe3726'}}}