```json
{
  "id": "b0190bcf23d764ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294604,
  "host_pid": "9e6742732c60:1",
  "hash": "87a9d1e160f884384af6dab3ec6fd2913b62f659910130329513944d3809a3dc",
  "cid": "QmV187a9d1e160f884384af6dab3ec6fd2913b62f659",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294604,
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
      "evaluated_at": 1760294604
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
  "sig": "40faa1c7fe77052ef7a0316de02c139613b478f77b1489b38c0323515a912e8a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151593614
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 99805812, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': '43945ca7b36522b2'}}}