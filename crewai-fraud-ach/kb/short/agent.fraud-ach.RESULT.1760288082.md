```json
{
  "id": "119223f34e6f1918",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288082,
  "host_pid": "9e6742732c60:1",
  "hash": "43ef2320f8bf4cf4c577ec2f7ab28a88a0db556fce68a3b0935e67c014534c0f",
  "cid": "QmV143ef2320f8bf4cf4c577ec2f7ab28a88a0db556f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288082,
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
      "evaluated_at": 1760288082
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
  "sig": "54e7a9f61ece6be1a218b66ee7314914883d96c7cdb28ac8da69242de8510dfb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242854691
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 15159750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285765, 'matching_hash': '6f29fe2a1ce5e88d'}}}