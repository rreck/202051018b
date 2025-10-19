```json
{
  "id": "aa1a6d920b211426",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293552,
  "host_pid": "9e6742732c60:1",
  "hash": "06e4feca993e01be6788440d96a6ba209f8310a00c44bc50135629dc399f29af",
  "cid": "QmV106e4feca993e01be6788440d96a6ba209f8310a0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293552,
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
      "evaluated_at": 1760293552
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
  "sig": "833173daa21903e026e048604fb829ec8c0a3dd95f3e32b3e87e8151f6ee536d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249862639
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 76016265, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '8cd9f1a7b8ce269f'}}}