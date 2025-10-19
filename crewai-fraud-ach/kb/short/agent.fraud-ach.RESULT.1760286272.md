```json
{
  "id": "5c996bb65b252545",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286272,
  "host_pid": "9e6742732c60:1",
  "hash": "3f27f6bc1531048ce9449528e8262a2f772de827b117942abf5a3464956c06b9",
  "cid": "QmV13f27f6bc1531048ce9449528e8262a2f772de827",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286272,
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
      "evaluated_at": 1760286272
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
  "sig": "43f64cff798753187d47497c3e67ca796787dead2aa74b2d9f6047282009efcf"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000024349722
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285763, 'matching_hash': '3e275568f5204778'}}}