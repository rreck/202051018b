```json
{
  "id": "1ee4e43b881ba555",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290009,
  "host_pid": "9e6742732c60:1",
  "hash": "074726c5d9d82c94e2eeff2e93cd38960b27f49675b02d6dbf57469f8da8b62f",
  "cid": "QmV1074726c5d9d82c94e2eeff2e93cd38960b27f496",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290009,
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
      "evaluated_at": 1760290009
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
  "sig": "b1d0a6539ef905944a7d0db4102d307fd326d844c02e923e0e2f1ff68f645b1f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464749166
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 49569068, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285764, 'matching_hash': '2c72b457e71ecad2'}}}