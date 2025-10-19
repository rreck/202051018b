```json
{
  "id": "45e1e6e0f8b8924e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291893,
  "host_pid": "9e6742732c60:1",
  "hash": "97881ad885b46081cad44085d5976f8f18d8a563ce0800798327292a56b87b9d",
  "cid": "QmV197881ad885b46081cad44085d5976f8f18d8a563",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291893,
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
      "evaluated_at": 1760291893
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
  "sig": "099750df3ba6cbae51e477baed406b63e044675dda7c6680fa5fce351d3fe806"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276932154
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 68100350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285765, 'matching_hash': '117d4b1b88487dad'}}}