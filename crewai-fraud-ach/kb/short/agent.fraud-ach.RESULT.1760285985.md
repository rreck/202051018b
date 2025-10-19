```json
{
  "id": "769947058e238fbd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285985,
  "host_pid": "9e6742732c60:1",
  "hash": "a0b16b240f569a12021df797e961069382da166d51f1238ef3b4c3297a9862c9",
  "cid": "QmV1a0b16b240f569a12021df797e961069382da166d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285985,
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
      "evaluated_at": 1760285985
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
  "sig": "9d59a202a505ed06781264290eaa5c85757928b855976eb8ea4e257314f5d00d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000024542500
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285765, 'matching_hash': 'f616428a070fc3ba'}}}