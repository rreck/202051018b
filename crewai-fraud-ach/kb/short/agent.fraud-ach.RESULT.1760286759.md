```json
{
  "id": "622f6aa173fa5249",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286759,
  "host_pid": "9e6742732c60:1",
  "hash": "45367facfd83e89af01879300fb39ccff1261652ae7341a1b5db589112849eb4",
  "cid": "QmV145367facfd83e89af01879300fb39ccff1261652",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286759,
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
      "evaluated_at": 1760286759
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
  "sig": "0012e7464154b5a59425249ff37e5ae78fd0e2f07ddfc8bfea53a03ec3dbe555"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000245381675
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285765, 'matching_hash': 'fa6674ee96d393a2'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285763, 'matching_hash': '7a27d1bb592c5069'}}}