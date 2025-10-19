```json
{
  "id": "b7f00ce81335bc6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288143,
  "host_pid": "9e6742732c60:1",
  "hash": "b05eeb10e382cc0b84c5a899d08255d3c883692d9174e880cad1a7c1e06fd61f",
  "cid": "QmV1b05eeb10e382cc0b84c5a899d08255d3c883692d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288143,
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
      "evaluated_at": 1760288143
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
  "sig": "5a999025d8c50ce63b4691f5168069b799383d19fd66ad9cee5e36b526923a25"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032976698
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 31191972, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285764, 'matching_hash': 'b86b53820ba813a1'}}}