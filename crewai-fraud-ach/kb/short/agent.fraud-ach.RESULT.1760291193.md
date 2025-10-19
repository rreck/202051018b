```json
{
  "id": "4a75b812e6f28773",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291193,
  "host_pid": "9e6742732c60:1",
  "hash": "82694b668a4a60c249608fc4c3a06ef9ff4df61414d1c6af09a10451b4f409db",
  "cid": "QmV182694b668a4a60c249608fc4c3a06ef9ff4df614",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291193,
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
      "evaluated_at": 1760291193
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
  "sig": "fdcf7dc5b83ddecc58464ffcd2b2959121e5d3dffdcbb27e184046eff75f2ec8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597950940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 45024473, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285763, 'matching_hash': 'cd3d42208c2780a3'}}}