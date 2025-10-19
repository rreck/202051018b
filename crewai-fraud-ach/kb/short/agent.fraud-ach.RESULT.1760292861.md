```json
{
  "id": "bb53c9a5f6361e24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292861,
  "host_pid": "9e6742732c60:1",
  "hash": "6622a52aab351ba860cb4ac2110ccbe106956584497d098daa52338955fd625e",
  "cid": "QmV16622a52aab351ba860cb4ac2110ccbe106956584",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292861,
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
      "evaluated_at": 1760292861
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
  "sig": "bf741f7bd1da5039a20f367126b562258f42bdb1cdb48d7b96256530ecd307e3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 65559088, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}