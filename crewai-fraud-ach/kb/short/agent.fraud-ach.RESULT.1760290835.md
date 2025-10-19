```json
{
  "id": "7f41b86b29b4ce54",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290835,
  "host_pid": "9e6742732c60:1",
  "hash": "008d821d1d4f4a13cbe88839c044ceda92c76d0221d6bb6839a095d7499b6027",
  "cid": "QmV1008d821d1d4f4a13cbe88839c044ceda92c76d02",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290835,
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
      "evaluated_at": 1760290835
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
  "sig": "b3ca97d1df434aa2f0b883621233a6b3e8f2b4d0d7339739a51883d71ccbbf8a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023386962
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 16000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285765, 'matching_hash': '663df3e5258a7a87'}}}