```json
{
  "id": "b55fd5e47a19d412",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293978,
  "host_pid": "9e6742732c60:1",
  "hash": "5ba4395cf9d1cc4f2f226b586d2ad0f424148ff947907157ec808e40e9be40e9",
  "cid": "QmV15ba4395cf9d1cc4f2f226b586d2ad0f424148ff9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293978,
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
      "evaluated_at": 1760293978
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
  "sig": "e525414cc3db8ae758f1bec692655cbd03e3f4b0d822f443e183604c164dd21c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467602006
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 106261267, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285765, 'matching_hash': 'cc8ab13ff4b154cd'}}}