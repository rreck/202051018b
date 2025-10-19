```json
{
  "id": "af8baf9427fff67c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291446,
  "host_pid": "9e6742732c60:1",
  "hash": "a4a1bd477acc696d18c8c9e5abb6da0089068fe8441a065d966e026e0c2f8ed2",
  "cid": "QmV1a4a1bd477acc696d18c8c9e5abb6da0089068fe8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291446,
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
      "evaluated_at": 1760291446
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
  "sig": "9823fe94944ad204c8bbe61767718a5db8b22d8d86822461c97bfc21d0bd33d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032306947
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 13493375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': '0095d1181b74b3e8'}}}