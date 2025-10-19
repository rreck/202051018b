```json
{
  "id": "dffe9883f9eda1d9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286034,
  "host_pid": "9e6742732c60:1",
  "hash": "ff4739ce9ec7b70f978c28fd59ef1b155e64e1db2fe65411a4a7868dbc151c1c",
  "cid": "QmV1ff4739ce9ec7b70f978c28fd59ef1b155e64e1db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286034,
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
      "evaluated_at": 1760286034
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
  "sig": "d16e9bfe8db0ee35770a58c3da43cf7a198f4a1f130bf424d0da047619fa34da"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009593439832
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 11, 'first_seen': 1760285763, 'matching_hash': '7b717df8c1c9c887'}}} 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760284979, 'matching_hash': '98c544a6e0691c0b'}}}