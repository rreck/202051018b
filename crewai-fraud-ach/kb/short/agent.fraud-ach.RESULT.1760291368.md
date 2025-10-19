```json
{
  "id": "e78f020384a17c76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291368,
  "host_pid": "9e6742732c60:1",
  "hash": "fd1ce830478eff00c7c5a9ba7f01e2b47ab97520de8c3f31f2096d0b1dbb3a33",
  "cid": "QmV1fd1ce830478eff00c7c5a9ba7f01e2b47ab97520",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291368,
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
      "evaluated_at": 1760291368
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
  "sig": "0d0404a769e466b9546112d98e8418a6a316735b8bca7206bcf28825b12549c3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593870321
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 14233575, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': 'ac61827ecd1197f0'}}}