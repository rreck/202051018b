```json
{
  "id": "25de29bfd219575d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290516,
  "host_pid": "9e6742732c60:1",
  "hash": "ac09449b2d0aed5ccbba59a23fec4f024eca57298c86cad41b310a9d59704226",
  "cid": "QmV1ac09449b2d0aed5ccbba59a23fec4f024eca5729",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290516,
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
      "evaluated_at": 1760290516
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
  "sig": "83933f5d55f94ee1fb1254e767203b3bb262f0119e3aa197eba9e281426808cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241561723
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 13235856, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285764, 'matching_hash': '61d0611cbf39c4a3'}}}