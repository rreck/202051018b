```json
{
  "id": "3405b1824b65884c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290362,
  "host_pid": "9e6742732c60:1",
  "hash": "890994efa3788a03276f82edc2947580d588d203460de1aadfa0504fc0bdc3d3",
  "cid": "QmV1890994efa3788a03276f82edc2947580d588d203",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290362,
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
      "evaluated_at": 1760290362
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
  "sig": "68dd1986ef8653c8aae944ae6deb09840d95608fd498ab62d8f6f908d5529636"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155748621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 68778708, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285764, 'matching_hash': 'df4db45348ec5c9a'}}}