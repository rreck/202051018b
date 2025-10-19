```json
{
  "id": "f92c0786d26cddcd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286285,
  "host_pid": "9e6742732c60:1",
  "hash": "fd8570575c91a03a314ded4cb99e57660565500258f9162294f500dfd412bb39",
  "cid": "QmV1fd8570575c91a03a314ded4cb99e576605655002",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286285,
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
      "evaluated_at": 1760286285
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
  "sig": "b2ce0477d9ca23bb75463ef3f63622559ee09159e264083f0331ce93806f58b9"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009590866940
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 19, 'first_seen': 1760285765, 'matching_hash': '66ff896a34603a53'}}}