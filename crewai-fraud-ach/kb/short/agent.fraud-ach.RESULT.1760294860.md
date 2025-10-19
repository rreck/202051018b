```json
{
  "id": "a1debc578d510e08",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294860,
  "host_pid": "9e6742732c60:1",
  "hash": "5cdb9d8fed6f811346c0ed3ee20b44e4430df9f6b15c0c3976b239a2d71db6b8",
  "cid": "QmV15cdb9d8fed6f811346c0ed3ee20b44e4430df9f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294860,
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
      "evaluated_at": 1760294860
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
  "sig": "ae8bf862960242cdf21d85e4e991d67de9f6d45d6765199c443d82214ff77309"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244506997
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 85119936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '00a59e186c59db13'}}}