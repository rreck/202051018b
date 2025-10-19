```json
{
  "id": "8be84deb35e14f03",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285124,
  "host_pid": "9e6742732c60:1",
  "hash": "994362f5efdce664af1dff106a604aa7248669920720fe15b46f640a26a42d7f",
  "cid": "QmV1994362f5efdce664af1dff106a604aa724866992",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285124,
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
      "evaluated_at": 1760285124
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
  "sig": "cbe5eb689fbbe97eef62d2cdaeee504e8bb96d6543cb26e39e67a7d66be3823d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}