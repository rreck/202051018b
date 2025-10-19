```json
{
  "id": "febb643c2a816db0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294572,
  "host_pid": "9e6742732c60:1",
  "hash": "5ce70ec132bdfd5ca3a11a5e15457aff9185ae79d4cd0cec9a96a860ff4418c8",
  "cid": "QmV15ce70ec132bdfd5ca3a11a5e15457aff9185ae79",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294572,
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
      "evaluated_at": 1760294572
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
  "sig": "e7bf178d9fdd0ceb14a15100ca7aecb55c3c44f3cd29b6c596d0d16faba8bbbd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465368597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 59697120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285765, 'matching_hash': 'f57f84d557436d23'}}}