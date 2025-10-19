```json
{
  "id": "7024acc6a58d1eb8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294184,
  "host_pid": "9e6742732c60:1",
  "hash": "dd7c8bbf9f12a99324e329adcf60d6b131ae09ea616c74ee787fb21ef950692c",
  "cid": "QmV1dd7c8bbf9f12a99324e329adcf60d6b131ae09ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294184,
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
      "evaluated_at": 1760294185
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
  "sig": "c64096cad3be928967e1d19fc18e0dbfd0607ed1a5cb85da19fce0b70914a528"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248509249
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 38341548, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285764, 'matching_hash': '3102d5e76c589166'}}}