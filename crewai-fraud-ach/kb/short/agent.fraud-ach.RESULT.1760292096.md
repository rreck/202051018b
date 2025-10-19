```json
{
  "id": "004789f47c85015d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292096,
  "host_pid": "9e6742732c60:1",
  "hash": "33294d7a87efb0cbd23ed9446cb90369ef684622bda020f16dc54c4e797a1df6",
  "cid": "QmV133294d7a87efb0cbd23ed9446cb90369ef684622",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292096,
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
      "evaluated_at": 1760292096
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
  "sig": "4281d9f21f1555aff8893c96b7e7a9dc1f399b303df67cce146da8213d665d4f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242854691
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 35126250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285765, 'matching_hash': '6f29fe2a1ce5e88d'}}}