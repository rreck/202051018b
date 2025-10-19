```json
{
  "id": "1f6ede1c57076391",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287555,
  "host_pid": "9e6742732c60:1",
  "hash": "16d2d45a272d648818c7e53669d57f91e52b1b9ede74473a14f5bb0e50405241",
  "cid": "QmV116d2d45a272d648818c7e53669d57f91e52b1b9e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287555,
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
      "evaluated_at": 1760287555
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
  "sig": "3c59fadb59a275aa2e7215a61baf18cdb66d9d89a8356942b99cf86513e6a28b"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 111000023966417
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 29110016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285764, 'matching_hash': 'bf59b19c5a8c3ed8'}}}