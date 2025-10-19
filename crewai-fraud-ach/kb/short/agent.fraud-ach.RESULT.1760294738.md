```json
{
  "id": "da7c6b7d48212656",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294738,
  "host_pid": "9e6742732c60:1",
  "hash": "ad3bc7d3bf277cd91f152c626df60b0ab15f0559a6828c443d44a8f76a176a50",
  "cid": "QmV1ad3bc7d3bf277cd91f152c626df60b0ab15f0559",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294738,
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
      "evaluated_at": 1760294738
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
  "sig": "a855f61fb4fc9348646d6a86dbf7668aebe35639f52137f9c8baa8b7aa0238e2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 77334264, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}