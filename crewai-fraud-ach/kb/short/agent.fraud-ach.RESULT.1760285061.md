```json
{
  "id": "8450f5173a1a8b16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285061,
  "host_pid": "9e6742732c60:1",
  "hash": "bcf3c816ab4b7762fa3386a575a10d147f19be3c87dba10d57d6d439bf8b4061",
  "cid": "QmV1bcf3c816ab4b7762fa3386a575a10d147f19be3c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285061,
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
      "evaluated_at": 1760285061
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
  "sig": "f54b5fffee3a9bebad47312cc06a61e0268fbd1142f593697aeb9968069c3a72"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}