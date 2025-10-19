```json
{
  "id": "d06e02f82ff1efe8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291318,
  "host_pid": "9e6742732c60:1",
  "hash": "df3e144099a08f21e29f6d5bb64fed9e4d906b4b479a028076c96dca4ce1661c",
  "cid": "QmV1df3e144099a08f21e29f6d5bb64fed9e4d906b4b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291318,
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
      "evaluated_at": 1760291318
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
  "sig": "9114c0435ef172838c4a19fe607573d36e27185a5ef1dff887c3323bd504d018"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022462179
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 69801900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': 'b017d6ab8abfffc0'}}}