```json
{
  "id": "30acef1cad95caf6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291568,
  "host_pid": "9e6742732c60:1",
  "hash": "7e479b380e842706e10dc39d3fdff90e4d83c8941024bd8c20e4740710fddd26",
  "cid": "QmV17e479b380e842706e10dc39d3fdff90e4d83c894",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291568,
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
      "evaluated_at": 1760291568
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
  "sig": "0050d4ba8c9f4169f7487556296f730cec412b1458d58a70d46f83a34f3cd6f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598799064
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 66976416, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285763, 'matching_hash': '14e8b5e643b0ea13'}}}