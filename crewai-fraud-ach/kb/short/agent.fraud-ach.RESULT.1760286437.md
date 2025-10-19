```json
{
  "id": "019a91c970c14111",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286437,
  "host_pid": "9e6742732c60:1",
  "hash": "910ccb5e8684859757bb52ce2266c06505f4ab8a5ae80e7121e239f99ca8a7d1",
  "cid": "QmV1910ccb5e8684859757bb52ce2266c06505f4ab8a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286437,
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
      "evaluated_at": 1760286437
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
  "sig": "d4927111eff6605625d7eb5030de87da6c66b877b7f57709d5ad4ff96bc87730"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105157316048
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285764, 'matching_hash': '8f4887477877b00a'}}}