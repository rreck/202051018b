```json
{
  "id": "fbc14ac849b41f6c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286346,
  "host_pid": "9e6742732c60:1",
  "hash": "9b1f8b02c62fa12f32aba76cdbd1a48101303f563c44a5da4407d3120157190a",
  "cid": "QmV19b1f8b02c62fa12f32aba76cdbd1a48101303f56",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286346,
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
      "evaluated_at": 1760286346
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
  "sig": "deda4fa91fb07ea0f1976bbc6069eba987f09183822d3b3d532e00b4f1ba590d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000029236644
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285765, 'matching_hash': 'c69cf0de1758a1d7'}}}