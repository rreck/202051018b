```json
{
  "id": "a2e298ab7554f119",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290522,
  "host_pid": "9e6742732c60:1",
  "hash": "65bdbe3626757778760e6674fdac176b1965f4b29a67439bf4203e1e4a48261e",
  "cid": "QmV165bdbe3626757778760e6674fdac176b1965f4b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290522,
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
      "evaluated_at": 1760290522
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
  "sig": "ab5ddf41e6a42e87d83f7474bb678b24b8f7a617e0d488ee50c12bcce2a1e981"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033965137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 21687360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285765, 'matching_hash': 'a94abbf708458614'}}}