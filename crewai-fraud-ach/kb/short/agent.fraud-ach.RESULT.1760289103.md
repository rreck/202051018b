```json
{
  "id": "296744324d7af3df",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289103,
  "host_pid": "9e6742732c60:1",
  "hash": "9cbb2f2b0d73f734cd953e2e3b3c989437a941d2ef9fd95f131f087f9534335f",
  "cid": "QmV19cbb2f2b0d73f734cd953e2e3b3c989437a941d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289103,
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
      "evaluated_at": 1760289103
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
  "sig": "74d251a595770c784e2c662abd1c3401c89089a115a16b017bc95d5f4bd056ec"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594254224
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 13660683, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285765, 'matching_hash': 'a2bdc2eb52125893'}}}