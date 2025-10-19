```json
{
  "id": "1858e79191ae4ea9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287973,
  "host_pid": "9e6742732c60:1",
  "hash": "d597d60d2cd807f97b8680f7fa3489f6cb1fcc9026bd45b2f2004af34493d3bf",
  "cid": "QmV1d597d60d2cd807f97b8680f7fa3489f6cb1fcc90",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287973,
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
      "evaluated_at": 1760287973
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
  "sig": "bae6a45bec34c00c0bb1d0f5c9cb7150b6b3fa0af99ebb6bfd0a5ee4f7d61820"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150171825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 14661582, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285765, 'matching_hash': 'da3473f59eec3040'}}}