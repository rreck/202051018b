```json
{
  "id": "c8ea769750428ee4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289435,
  "host_pid": "9e6742732c60:1",
  "hash": "8a366dd4d29aeb497081298f65bd5842113965d15c6b340cf0272b1c03b7ca2e",
  "cid": "QmV18a366dd4d29aeb497081298f65bd5842113965d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289435,
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
      "evaluated_at": 1760289435
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
  "sig": "c74028efc7c6985b044279a13f2ee7db38112bb77c174fee65e62c0ad09e583b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245017605
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 57862398, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285763, 'matching_hash': '04117a7715fe8402'}}}