```json
{
  "id": "0ac407c905f1ab9f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290001,
  "host_pid": "9e6742732c60:1",
  "hash": "6f852564bf4a6a38fc73f06eab773f47bcf9537aa0996710ed655bf0a70c793c",
  "cid": "QmV16f852564bf4a6a38fc73f06eab773f47bcf9537a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290001,
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
      "evaluated_at": 1760290001
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
  "sig": "d897cb3e25e61249b98a35322d38ba313d2324f69f7d58407e795a8a86cca839"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031517905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 61931589, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285763, 'matching_hash': 'e8f76fb2eb784ea5'}}}