```json
{
  "id": "69d887d65b5b3704",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290198,
  "host_pid": "9e6742732c60:1",
  "hash": "79cee7d212fec47404ed160e021aa9d0c85f8a216433f4f881fd1a1dedf914c7",
  "cid": "QmV179cee7d212fec47404ed160e021aa9d0c85f8a21",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290198,
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
      "evaluated_at": 1760290198
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
  "sig": "3c4f233d3dde9b030518f4e4509adff4e2fd076eab93d0656d9d0b879122cae2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598880520
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 27426816, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285764, 'matching_hash': '9fe1b03994749115'}}}