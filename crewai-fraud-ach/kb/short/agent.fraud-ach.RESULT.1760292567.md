```json
{
  "id": "2839959c3a97e7cf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292567,
  "host_pid": "9e6742732c60:1",
  "hash": "3c1e65b60a98587c2b4b73e8f869c74943c71e12a5046bd3604f96a4c0b8174e",
  "cid": "QmV13c1e65b60a98587c2b4b73e8f869c74943c71e12",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292567,
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
      "evaluated_at": 1760292567
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
  "sig": "a311e0efaa623ec78abacae60b4b70da7d2c6eaec49a5bcf0268463fc2bf164c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241561723
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 17415600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285764, 'matching_hash': '61d0611cbf39c4a3'}}}