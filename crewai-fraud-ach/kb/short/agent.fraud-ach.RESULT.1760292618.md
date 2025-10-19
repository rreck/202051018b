```json
{
  "id": "57f4aa85dc223bac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292618,
  "host_pid": "9e6742732c60:1",
  "hash": "5bfb8b651d78c8f3dc2a9b886abf22bdb986b0f119b57f9bf0a98cbe94ef0fb0",
  "cid": "QmV15bfb8b651d78c8f3dc2a9b886abf22bdb986b0f1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292618,
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
      "evaluated_at": 1760292618
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
  "sig": "d0a81fda3da19bbb3afa7e87fc20019b2f845aaff9300ce7c870440a9ad5a797"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027147487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 100460604, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285765, 'matching_hash': 'f2056111b893f4fa'}}}