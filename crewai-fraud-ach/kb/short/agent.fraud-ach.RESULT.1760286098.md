```json
{
  "id": "e15279cc65f1781d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286098,
  "host_pid": "9e6742732c60:1",
  "hash": "000f7d05f866ab87bf780d202a7750bc6c08a6e7dc3606825a4552eb29d7dfac",
  "cid": "QmV1000f7d05f866ab87bf780d202a7750bc6c08a6e7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286098,
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
      "evaluated_at": 1760286098
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
  "sig": "dd4fcdbc0756e9acbbf0cad187e66bcd0f000dc7ac69627a0cc695538449c939"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201467874144
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 13, 'first_seen': 1760285764, 'matching_hash': '428cbf79813503ca'}}}