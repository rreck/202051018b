```json
{
  "id": "de0c7bc685accac4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287809,
  "host_pid": "9e6742732c60:1",
  "hash": "97a2ab8df8b4169caf9900e3162a6d8e10c737921b03fecb6f7ada38fc428d94",
  "cid": "QmV197a2ab8df8b4169caf9900e3162a6d8e10c73792",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287809,
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
      "evaluated_at": 1760287809
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
  "sig": "66de5870ed98777b1fc1663f3721bb83bd104f21b2cd32afaabaf77aaf8582ad"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 111000026198505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 34193273, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285764, 'matching_hash': '8ff7ad30241d2e02'}}}