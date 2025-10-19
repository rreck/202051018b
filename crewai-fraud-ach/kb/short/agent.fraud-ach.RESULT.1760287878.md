```json
{
  "id": "2435b24175ccfa30",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287878,
  "host_pid": "9e6742732c60:1",
  "hash": "5674de716af9457bc98a514ff16fa4aed0ec461a0afb6739603734ef80a25ce2",
  "cid": "QmV15674de716af9457bc98a514ff16fa4aed0ec461a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287878,
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
      "evaluated_at": 1760287878
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
  "sig": "fcb212e333f3e69f9105149eaa08f646e9a8cb7c39c3cc402450f921d9dfbd19"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596862432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 15304200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285764, 'matching_hash': 'ec6d2f2d96a1a77c'}}}