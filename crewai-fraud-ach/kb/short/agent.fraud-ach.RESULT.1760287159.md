```json
{
  "id": "09943a48b837a987",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287159,
  "host_pid": "9e6742732c60:1",
  "hash": "b8ff71d3fe288389b68c234bd7539817c16d1b109892d2010ea10ea6ea3bf957",
  "cid": "QmV1b8ff71d3fe288389b68c234bd7539817c16d1b10",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287159,
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
      "evaluated_at": 1760287159
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
  "sig": "1469e5b09812ec4e127fef72da60ec430a5357d0fd62795149513411c0f78e8c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105154990255
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285763, 'matching_hash': '800f0de895a214ba'}}}