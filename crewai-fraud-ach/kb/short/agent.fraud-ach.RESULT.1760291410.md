```json
{
  "id": "5c009a83cbabee81",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291410,
  "host_pid": "9e6742732c60:1",
  "hash": "84f29d76a59774c5035040749d25efbe01ea316fdad08aff3e7c8d7024bd88bc",
  "cid": "QmV184f29d76a59774c5035040749d25efbe01ea316f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291410,
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
      "evaluated_at": 1760291410
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
  "sig": "131fc4112da7b1426eef0c9998999da223dc4786624b9f728d3878738c17891b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271648434
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 41186322, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285763, 'matching_hash': '7a167e1c4ddc5d6e'}}}