```json
{
  "id": "4bb44f44e82656ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289152,
  "host_pid": "9e6742732c60:1",
  "hash": "75c5220c22a391f40196a7a91f6130cb2538043169d3ffe8238956a38566390a",
  "cid": "QmV175c5220c22a391f40196a7a91f6130cb25380431",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289152,
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
      "evaluated_at": 1760289152
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
  "sig": "d177b50480a91a99f3f971fd6251f8cd1971dec92b38e4dff604bd9ab0667453"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027679172
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 49939670, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285763, 'matching_hash': 'bcf2a51730a73925'}}}