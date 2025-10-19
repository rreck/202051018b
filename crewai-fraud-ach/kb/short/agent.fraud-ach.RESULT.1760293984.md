```json
{
  "id": "24abee6ae149dd9f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293984,
  "host_pid": "9e6742732c60:1",
  "hash": "f7cf4aa608b64f6385c165d793be1830f154a0ff706dcf4b3601580f8c7a6b7f",
  "cid": "QmV1f7cf4aa608b64f6385c165d793be1830f154a0ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293984,
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
      "evaluated_at": 1760293984
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
  "sig": "2fef177cce5bcadb3896bccfd0c4ea8a4a46a50b53f5fd9feec27b2a34c41a3b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598290210
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 14671343, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285765, 'matching_hash': '255d3759171e1aec'}}}