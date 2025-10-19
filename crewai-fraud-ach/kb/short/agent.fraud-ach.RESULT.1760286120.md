```json
{
  "id": "5c66a15fce0ccc50",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286120,
  "host_pid": "9e6742732c60:1",
  "hash": "263b14a39a21976d516b379f979330966ef0f972745443d04a39e0a91e8e8c92",
  "cid": "QmV1263b14a39a21976d516b379f979330966ef0f972",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286120,
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
      "evaluated_at": 1760286120
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "d9956405e9cdc959feffa4a453b907d350cf8f94eb8d3b5476856c26c5e6ea4c"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 244163284273009
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': '5b6cb55161b8e1f8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244163284', 'validation_error': 'Invalid routing number checksum'}}}