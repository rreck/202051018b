```json
{
  "id": "ddad255ce9cc4951",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285155,
  "host_pid": "9e6742732c60:1",
  "hash": "fe5ea147162a7b85f67c919781957a4a307bce8f5cd2569692be6039bfb39b8f",
  "cid": "QmV1fe5ea147162a7b85f67c919781957a4a307bce8f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285155,
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
      "evaluated_at": 1760285155
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
  "sig": "fcc615062965e10cd5ff841ffda9e181b6363ccc273557533f64b609294dd52e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}