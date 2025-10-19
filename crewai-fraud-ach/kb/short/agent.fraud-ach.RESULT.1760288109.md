```json
{
  "id": "8b29bfa907a7a96f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288109,
  "host_pid": "9e6742732c60:1",
  "hash": "36ba56079c249e601019e05fc3cec27a5c003b9b460dcdd757c4faa533c4046f",
  "cid": "QmV136ba56079c249e601019e05fc3cec27a5c003b9b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288109,
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
      "evaluated_at": 1760288109
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
  "sig": "e3a8c90ca1e7622b244c712f674b4ad024d1a55bbdde68260ba451493130917b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461315278
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 20148914, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285763, 'matching_hash': 'd87579b8c6b654cb'}}}