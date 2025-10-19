```json
{
  "id": "3546ba478eba0665",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293279,
  "host_pid": "9e6742732c60:1",
  "hash": "0fc2f9d5a107a774058e8b218b6f7cc84a08d963ba3dafba88aa5224244ec5f5",
  "cid": "QmV10fc2f9d5a107a774058e8b218b6f7cc84a08d963",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293279,
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
      "evaluated_at": 1760293279
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
  "sig": "0f6424e4daca882563a2ec1c23094cfc1403985c18c8756372b1b4b0d36ded85"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278037585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 22836440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '27cb7a10328c75d5'}}}