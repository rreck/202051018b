```json
{
  "id": "3199b0a618837bf2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288363,
  "host_pid": "9e6742732c60:1",
  "hash": "fa1db14d4984e7006c1bcc36da6b59543b9143dd653aa7751609be617bc4de08",
  "cid": "QmV1fa1db14d4984e7006c1bcc36da6b59543b9143dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288363,
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
      "evaluated_at": 1760288363
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
  "sig": "cad9e91980d8617ce1751a69095eff8b1547ae6960c06a93190f2e325360e4a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021479776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 20978776, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285763, 'matching_hash': '6c002fd60c3e5dde'}}}