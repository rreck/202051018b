```json
{
  "id": "7d00e9da8bd51ab3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286726,
  "host_pid": "9e6742732c60:1",
  "hash": "b2d13676b52cc63691b90b6724f31f59104741b61079ed2ab75ee70e6a3c9c26",
  "cid": "QmV1b2d13676b52cc63691b90b6724f31f59104741b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286726,
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
      "evaluated_at": 1760286726
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "151165bc8c20eddcd523ab17f72c6166340137d4f4ea500cfc3fbf20a5362934"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000242680908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12066530, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285764, 'matching_hash': '8e78dc9e18bacaa7'}}}