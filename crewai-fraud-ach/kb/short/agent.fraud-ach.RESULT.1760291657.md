```json
{
  "id": "dbd332164f970212",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291657,
  "host_pid": "9e6742732c60:1",
  "hash": "8c4a2ddf9c9156a8985ae36aa4b43c0a38b69b0cd27851132fdd637c1987d789",
  "cid": "QmV18c4a2ddf9c9156a8985ae36aa4b43c0a38b69b0c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291657,
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
      "evaluated_at": 1760291657
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
  "sig": "de99817c578c5dc9f9b04a8dabcc277e44870dbbda4849af9c25c422776a286a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242854691
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 33277500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285765, 'matching_hash': '6f29fe2a1ce5e88d'}}}