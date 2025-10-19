```json
{
  "id": "f4b18ebc9be48abd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285925,
  "host_pid": "9e6742732c60:1",
  "hash": "4153dda361699b50cc93cc824a596d6910e4f607efed2767e422def248375ab9",
  "cid": "QmV14153dda361699b50cc93cc824a596d6910e4f607",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285925,
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
      "evaluated_at": 1760285925
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
  "sig": "63d1501bb209e96e573ddeaaf59c9f1d25372160d2569817ce3c8f40d6cff1a8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201465368597
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285765, 'matching_hash': 'f57f84d557436d23'}}}