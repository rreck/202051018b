```json
{
  "id": "7800b7525a3a5a44",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292728,
  "host_pid": "9e6742732c60:1",
  "hash": "2bc709a33623de24ef298721aad326134b5dfdef6a02e91f1641c1116049d298",
  "cid": "QmV12bc709a33623de24ef298721aad326134b5dfdef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292728,
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
      "evaluated_at": 1760292728
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
  "sig": "5573115293b4157a3360638413c3dbd88ffe9ee04221f93dbe0afaeb97446882"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591278492
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 25444104, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': '3e8e4f28808ab222'}}}