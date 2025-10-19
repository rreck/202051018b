```json
{
  "id": "2e1747a7b4db6dc4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293486,
  "host_pid": "9e6742732c60:1",
  "hash": "d2fb9c6a9849af519f9732a70efdd59c19cd2330e5503da47f580785a941ffe2",
  "cid": "QmV1d2fb9c6a9849af519f9732a70efdd59c19cd2330",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293486,
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
      "evaluated_at": 1760293486
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
  "sig": "f3a2a8fcaba71a6ce322b07f21f72e04998a1eb99439693cdcf9870e449d707e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465368597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 54473622, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285765, 'matching_hash': 'f57f84d557436d23'}}}