```json
{
  "id": "273bf52eb025eb28",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286002,
  "host_pid": "9e6742732c60:1",
  "hash": "aec7549deb163c0acd04c204644d17eb9065af5d5cc0319d0832b0bdfd5d18ef",
  "cid": "QmV1aec7549deb163c0acd04c204644d17eb9065af5d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286002,
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
      "evaluated_at": 1760286002
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
  "sig": "fde9ee96ff820b8e9ca51428d4b328aa8ab9572c49c391a7ed5c5e1cd3a1d4f4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009599719457
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285763, 'matching_hash': '97e4873137c26cd1'}}}, 'risk_score': 85, 'details': {'duplicate_count': 10, 'first_seen': 1760285764, 'matching_hash': '39c5bac7d3007e29'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}