```json
{
  "id": "e679cdf5d8383c70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287065,
  "host_pid": "9e6742732c60:1",
  "hash": "17d695b1cc8f348e9c68a25c32efef1bf1b89b40fe7c2ce0302fadd656641705",
  "cid": "QmV117d695b1cc8f348e9c68a25c32efef1bf1b89b40",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287065,
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
      "evaluated_at": 1760287065
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
  "sig": "2ce5decec3b2dba82d6bc472a2de343b54dbbb531fb15d234482dee29c676568"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105159848459
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 46, 'first_seen': 1760285763, 'matching_hash': 'f6f76290fac8b474'}}}