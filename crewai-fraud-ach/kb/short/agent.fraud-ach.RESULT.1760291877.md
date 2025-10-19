```json
{
  "id": "937df088a01c1225",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291877,
  "host_pid": "9e6742732c60:1",
  "hash": "f5e9a62e1c7d38fc4486838f8591b7a62236a86186ebdfbf3a7b582cde3499da",
  "cid": "QmV1f5e9a62e1c7d38fc4486838f8591b7a62236a861",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291877,
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
      "evaluated_at": 1760291877
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
  "sig": "f28aa33baa69328ad5385e54cc3cd42806c55e7c94e619e7d564c3db088f9821"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158715464
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 27413485, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': '08e14bce24e2b1ea'}}}