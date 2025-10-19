```json
{
  "id": "375ec0a01052a3e8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293026,
  "host_pid": "9e6742732c60:1",
  "hash": "5cc26bedad2a3ab0984c282ff98988ef637123bb7c021d2e73ed6280e25e7dd5",
  "cid": "QmV15cc26bedad2a3ab0984c282ff98988ef637123bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293026,
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
      "evaluated_at": 1760293026
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
  "sig": "338d354294052c3b3fa5f665406f65a672b31400eec14e4ac079dab4136566b3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464168260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 31927980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285764, 'matching_hash': '4363f5d3ce380aeb'}}}