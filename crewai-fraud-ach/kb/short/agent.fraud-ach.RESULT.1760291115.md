```json
{
  "id": "ea2d83e2451a9e4a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291115,
  "host_pid": "9e6742732c60:1",
  "hash": "36c1f09350015584828ca80c9952f4a12d17adda7f35b9f4b9d418dda2184853",
  "cid": "QmV136c1f09350015584828ca80c9952f4a12d17adda",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291115,
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
      "evaluated_at": 1760291115
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
  "sig": "9d9108e798f0bd31c910da002adc9951e9359045d3d3c5d7b7de8bcf6169e86a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031029200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 10797886, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': '80e7fe619ff961e0'}}}