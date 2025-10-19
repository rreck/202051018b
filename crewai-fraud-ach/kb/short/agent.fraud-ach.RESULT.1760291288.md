```json
{
  "id": "0e21c904dcbfe2ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291288,
  "host_pid": "9e6742732c60:1",
  "hash": "f0f7be05794aa302526969d5e4bf0abf34773c36b98cf6ce313874e0718bf491",
  "cid": "QmV1f0f7be05794aa302526969d5e4bf0abf34773c36",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291288,
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
      "evaluated_at": 1760291288
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
  "sig": "98f18ee8e40cf8be234324abfbd49a31f1be44cacfec7d8782ce651f4494508f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039498282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 85199382, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285765, 'matching_hash': 'dad018b424b66512'}}}