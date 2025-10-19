```json
{
  "id": "83dfc44058f1dada",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288632,
  "host_pid": "9e6742732c60:1",
  "hash": "8bc8e45a4f68e662b47ebefb0d5d39c14cae93ec0c802b25c5fceda2a3d54340",
  "cid": "QmV18bc8e45a4f68e662b47ebefb0d5d39c14cae93ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288632,
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
      "evaluated_at": 1760288632
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
  "sig": "3571a3044f9f598561094d3c4f2f66e88e8c74dd001e756b1ebf036b97966835"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242987850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 11585871, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285764, 'matching_hash': 'ac2312cc15fe4af9'}}}