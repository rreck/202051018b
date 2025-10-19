```json
{
  "id": "fd48503d681c4c44",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287469,
  "host_pid": "9e6742732c60:1",
  "hash": "4bba2c45c22f588ccba107ccef3149a6be3ee4f0b69f7dd448bdac973a1d70f6",
  "cid": "QmV14bba2c45c22f588ccba107ccef3149a6be3ee4f0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287469,
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
      "evaluated_at": 1760287469
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "18f66bb54cba47565215edfc1bf6911401367dc854a0c072e7eca90fdd89ea08"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 031201468417432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 20722188, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285764, 'matching_hash': '3485380f8c896007'}}}