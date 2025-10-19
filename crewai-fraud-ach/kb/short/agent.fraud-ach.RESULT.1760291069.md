```json
{
  "id": "2eaa44de88aa44ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291069,
  "host_pid": "9e6742732c60:1",
  "hash": "a112b4c291aaa13c55083291918f80c92280e371d575fc4f58647dfb07051a52",
  "cid": "QmV1a112b4c291aaa13c55083291918f80c92280e371",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291069,
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
      "evaluated_at": 1760291069
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
  "sig": "9cba5fa1062355b1d4a876e31fc77fafb91cc9adaa360de73ecf163bf25da8b1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466272908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 62138946, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285765, 'matching_hash': 'c5e3c9a8e5c19188'}}}