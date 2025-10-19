```json
{
  "id": "ca8fa0dbe95f7f43",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290469,
  "host_pid": "9e6742732c60:1",
  "hash": "a6b3a09c390a63b19e1dc03d6211b473a1a49b547ade8751973a7275a1b18ec7",
  "cid": "QmV1a6b3a09c390a63b19e1dc03d6211b473a1a49b54",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290469,
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
      "evaluated_at": 1760290469
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
  "sig": "64ae4b0f66eff89184bd6566abd98d05ae3c5593f63af226450ceda2356bfed4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270162443
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 75051832, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285763, 'matching_hash': 'e637274c2d5e4084'}}}