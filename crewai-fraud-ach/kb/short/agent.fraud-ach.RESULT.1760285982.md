```json
{
  "id": "bf6f390ada977016",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285982,
  "host_pid": "9e6742732c60:1",
  "hash": "a9d10668ddc1d5c39861a377279c5aace9eb26f1963f549d3ab212ab903af2e6",
  "cid": "QmV1a9d10668ddc1d5c39861a377279c5aace9eb26f1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285982,
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
      "evaluated_at": 1760285982
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
  "sig": "4354066b09682f68c161bdef834885be9bff883342a27b5df360a6e6aca4d1d3"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000029278927
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285765, 'matching_hash': '45338af8ff50831c'}}}