```json
{
  "id": "21e9c356fdcf0522",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286722,
  "host_pid": "9e6742732c60:1",
  "hash": "f7b199c0c91565afa8918fcb479ac9d62d9f25ce4ecd8c63bf634e6a52868850",
  "cid": "QmV1f7b199c0c91565afa8918fcb479ac9d62d9f25ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286722,
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
      "evaluated_at": 1760286722
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
  "sig": "02e82bbbd231f9e8ba75cf757fb632b64070833d563eca9a34ebdc541f5f29e0"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000247162231
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285763, 'matching_hash': '92769f469bceb512'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285763, 'matching_hash': '152f3a2a027ae633'}}}