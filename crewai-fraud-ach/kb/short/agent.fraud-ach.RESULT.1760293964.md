```json
{
  "id": "eb1f9f92dff19e3c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293964,
  "host_pid": "9e6742732c60:1",
  "hash": "ccfc92d19d2c0d4834135601f0882e04f2e22305d0887f0d40051bf0aee56d9d",
  "cid": "QmV1ccfc92d19d2c0d4834135601f0882e04f2e22305",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293964,
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
      "evaluated_at": 1760293964
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
  "sig": "42756f29224f31e415b8b94ff82af410564a84a72606128d45a966f693fcd7ce"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245652457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 19473473, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285763, 'matching_hash': '6ac12dd8f1799493'}}}