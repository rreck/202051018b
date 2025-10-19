```json
{
  "id": "4fa5cc0e5558a063",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285952,
  "host_pid": "9e6742732c60:1",
  "hash": "1ceda11bc4c8e99ebc16010cc378a1358deb8a1adf245ce326d21869d2c4bda1",
  "cid": "QmV11ceda11bc4c8e99ebc16010cc378a1358deb8a1a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285952,
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
      "evaluated_at": 1760285952
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
  "sig": "24b2bb9dd87768f4447a90bda46958b2b436a077ade9486b965faaff652f705f"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000020807792
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285764, 'matching_hash': '8390351bce6e669b'}}}