```json
{
  "id": "e58ba527d11d2fac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286058,
  "host_pid": "9e6742732c60:1",
  "hash": "e71e9a0346d7b7896eca0331fd7e6be65ce46a029fd00bfd36951fe8c5c7f726",
  "cid": "QmV1e71e9a0346d7b7896eca0331fd7e6be65ce46a02",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286058,
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
      "evaluated_at": 1760286058
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
  "sig": "557a9a53d305a2145d27889208a75dd558e3023b1253424a5d0ea65686c077c6"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100270759086
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285763, 'matching_hash': 'eb79951538526d2c'}}}