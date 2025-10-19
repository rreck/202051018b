```json
{
  "id": "84c503f00f740958",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291984,
  "host_pid": "9e6742732c60:1",
  "hash": "ba97f26fc5769532775861051db052220dd7280a19166b7274f5b58f6bd9c55e",
  "cid": "QmV1ba97f26fc5769532775861051db052220dd7280a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291984,
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
      "evaluated_at": 1760291984
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
  "sig": "bf07026caabe54c811a6a1f5fa01a12e7bf400f16f732cc2dcf8aba0c07d4dd2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 59512376, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}