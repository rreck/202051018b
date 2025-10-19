```json
{
  "id": "9ea3eec7e5835bc0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293731,
  "host_pid": "9e6742732c60:1",
  "hash": "32bb3a71a87d176ac097d11c980aecd5c3453c2696def3422180df42c39cde19",
  "cid": "QmV132bb3a71a87d176ac097d11c980aecd5c3453c26",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293731,
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
      "evaluated_at": 1760293731
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
  "sig": "ee4b65ac25cc8b54580b9978a1faca608a99e93f8739c5544acb3eb96b8b9914"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241271841
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 96761504, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285764, 'matching_hash': '100dee2bbeee5c05'}}}