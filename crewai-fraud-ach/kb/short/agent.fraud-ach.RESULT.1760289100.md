```json
{
  "id": "207ec01241f6752d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289100,
  "host_pid": "9e6742732c60:1",
  "hash": "c5c5ffdf18d11451fa7651bdecb955968c962bebb45a9e3d9468f7aca79b2e4a",
  "cid": "QmV1c5c5ffdf18d11451fa7651bdecb955968c962beb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289100,
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
      "evaluated_at": 1760289100
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
  "sig": "7eb39501143f0a764073b498e4c10a6088c7ac2d953e91214cf7b2bb6a2da251"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020716291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 21366266, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285765, 'matching_hash': 'a2f2d41c7f22f612'}}}