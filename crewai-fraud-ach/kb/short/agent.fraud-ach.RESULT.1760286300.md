```json
{
  "id": "ba12285b4b29be86",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286300,
  "host_pid": "9e6742732c60:1",
  "hash": "976ba633d5c2b6c268ce180ee48fd6527bee55fb2f3d136194b402052272651e",
  "cid": "QmV1976ba633d5c2b6c268ce180ee48fd6527bee55fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286300,
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
      "evaluated_at": 1760286300
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
  "sig": "3f03f1499641a928c6d69263051bfd5238782c49f84855020f194a3f77cdeb5c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000020127754
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285763, 'matching_hash': '0e6816faa7d68d85'}}}