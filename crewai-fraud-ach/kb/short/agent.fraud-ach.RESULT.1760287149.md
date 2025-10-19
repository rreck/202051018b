```json
{
  "id": "0614e3d36c13e38f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287149,
  "host_pid": "9e6742732c60:1",
  "hash": "af3494c3d7dc1a2d2a8fefc2819fe1b17a332feab2cdbc378d315a4ab4e7b917",
  "cid": "QmV1af3494c3d7dc1a2d2a8fefc2819fe1b17a332fea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287149,
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
      "evaluated_at": 1760287149
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
  "sig": "35a4ffe983e30e3e6238887d322db2d88299f23ee366feaa4a13e697d51976ff"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009590985666
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10012950, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285763, 'matching_hash': 'a91912abaf20cb4f'}}}