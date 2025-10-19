```json
{
  "id": "eecbd7c4829aa471",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285849,
  "host_pid": "9e6742732c60:1",
  "hash": "89ed249732eeaab767b0cfb633c04ad3618e8502cc50c62560d2855be7db0103",
  "cid": "QmV189ed249732eeaab767b0cfb633c04ad3618e8502",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285849,
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
      "evaluated_at": 1760285849
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
  "sig": "31a4b0a5c4f978041afbcfef91b99e7395bef87eab2da22f9f073008343b6966"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000023265809
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 4, 'first_seen': 1760285763, 'matching_hash': 'c722b9853a03895a'}}}