```json
{
  "id": "769a8e1a122623ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294409,
  "host_pid": "9e6742732c60:1",
  "hash": "2de4771b2125042b22b34e779e0a8a4b11a5aee810b588f81b25620e1e4296ce",
  "cid": "QmV12de4771b2125042b22b34e779e0a8a4b11a5aee8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294409,
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
      "evaluated_at": 1760294409
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
  "sig": "f81702df6dc476eedcbca181183be63d6509dfef305cb27bc0ae8af416fe0443"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026908362
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 11850000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285765, 'matching_hash': '7a1f70b5e24e62dd'}}}