```json
{
  "id": "46486424291f4a38",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290634,
  "host_pid": "9e6742732c60:1",
  "hash": "9fcafb45591367a7bcb030976ccf6f964eef0cecafdb874c8f3d3f2710eea288",
  "cid": "QmV19fcafb45591367a7bcb030976ccf6f964eef0cec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290634,
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
      "evaluated_at": 1760290634
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
  "sig": "e6023462111a85eeeef1d1e1bc5f1e4aaf4e77aca44b52bc33e14cc68fe10277"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151422831
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 15845805, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285764, 'matching_hash': 'e9fc645b92693d6a'}}}