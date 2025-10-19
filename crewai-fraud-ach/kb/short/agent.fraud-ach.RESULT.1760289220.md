```json
{
  "id": "ffca53eacdae62a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289220,
  "host_pid": "9e6742732c60:1",
  "hash": "9724ddafd5f5404dc7fd8c2c0f95e667cb5a777da51bf696c15459bcecbbed02",
  "cid": "QmV19724ddafd5f5404dc7fd8c2c0f95e667cb5a777d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289220,
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
      "evaluated_at": 1760289220
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
  "sig": "4e99dd6c7c3883cdf7c1b8adf10559cc7f63d0cf6073a68a8f7dcab3b15b2d95"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027679172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 50808186, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285763, 'matching_hash': 'bcf2a51730a73925'}}}