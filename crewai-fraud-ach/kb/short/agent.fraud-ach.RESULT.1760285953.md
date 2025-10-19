```json
{
  "id": "f1ab8bde6cafe50e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285953,
  "host_pid": "9e6742732c60:1",
  "hash": "39eeb02650ca1ba0a1445b72fc0b38115032edecb23e08360385afeb705d4028",
  "cid": "QmV139eeb02650ca1ba0a1445b72fc0b38115032edec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285953,
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
      "evaluated_at": 1760285953
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
  "sig": "db31db5427b9d490481ff76f5ee727b6b55364d853afffe664a07a79e07a1b77"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000022109746
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285765, 'matching_hash': '2a578690bb80e431'}}}