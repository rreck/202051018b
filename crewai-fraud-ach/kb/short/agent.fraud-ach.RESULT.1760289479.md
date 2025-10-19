```json
{
  "id": "e0d8c13efefc652f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289479,
  "host_pid": "9e6742732c60:1",
  "hash": "993586257845488480358998747323277b425d9a52af26ece752bfe466edd5de",
  "cid": "QmV1993586257845488480358998747323277b425d9a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289479,
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
      "evaluated_at": 1760289479
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
  "sig": "26b336afe0eb48669f6916470776f38a516bdc945a3cf88ad2af603957947f35"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240022849
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 41348048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285765, 'matching_hash': 'fbe681be7d902297'}}}