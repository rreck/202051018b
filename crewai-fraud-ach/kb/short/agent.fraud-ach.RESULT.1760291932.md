```json
{
  "id": "0a4863109d89b585",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291932,
  "host_pid": "9e6742732c60:1",
  "hash": "8457814a6e49cbe61d4efac36fcf4232cc0c5542bb8fbc96b38ca3ddf9a539b0",
  "cid": "QmV18457814a6e49cbe61d4efac36fcf4232cc0c5542",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291932,
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
      "evaluated_at": 1760291932
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
  "sig": "cdbb2e959f59a8334e3bef0c31268614dae8c8ae6893f0707be6c168750fcdaa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596502557
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 20207784, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285764, 'matching_hash': 'c368684e8d9c7f24'}}}