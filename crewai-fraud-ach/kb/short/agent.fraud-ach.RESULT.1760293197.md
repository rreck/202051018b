```json
{
  "id": "292540333115f015",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293197,
  "host_pid": "9e6742732c60:1",
  "hash": "4afc2571b1e58af74633d35ae60ecc2c4e73bda362afdc29d28051cdf590d67d",
  "cid": "QmV14afc2571b1e58af74633d35ae60ecc2c4e73bda3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293197,
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
      "evaluated_at": 1760293197
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
  "sig": "bd13411aa1e5bf4758c2d4adb42c256c3309b1defe64e23c9c32f491176e3be4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594254224
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 25749783, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285765, 'matching_hash': 'a2bdc2eb52125893'}}}