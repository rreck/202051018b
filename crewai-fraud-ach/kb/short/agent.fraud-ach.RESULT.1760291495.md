```json
{
  "id": "68f142611d083976",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291495,
  "host_pid": "9e6742732c60:1",
  "hash": "e47ae19799f2f68443d3a9a0a1ab96d3c877f4dbd80db745acc62a3d60c2788a",
  "cid": "QmV1e47ae19799f2f68443d3a9a0a1ab96d3c877f4db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291495,
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
      "evaluated_at": 1760291495
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
  "sig": "422a10097baa0ee071e235186356ed7cd7e2fced791003ac8ba9c4ecce23766f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597735648
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 44326128, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285763, 'matching_hash': '529f1dc61ac58982'}}}