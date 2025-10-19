```json
{
  "id": "df987a3c2e8802c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287037,
  "host_pid": "9e6742732c60:1",
  "hash": "77ed21b6ffcd3d44dfa137640143e4ee85f9bacb6b03d0e272e86d1c306a23c3",
  "cid": "QmV177ed21b6ffcd3d44dfa137640143e4ee85f9bacb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287037,
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
      "evaluated_at": 1760287037
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
  "sig": "de8f9684807750b611247ec39606954cf737bb42783e408ead094c4f77dd9a25"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201460204606
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285763, 'matching_hash': '36d51f87c7d176f1'}}}